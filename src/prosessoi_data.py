import csv
import glob
import os
import json
import math
import argparse # Uusi kirjasto komentoriviparametreille

def calculate_bearing(lat1_deg, lon1_deg, lat2_deg, lon2_deg):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1_deg, lon1_deg, lat2_deg, lon2_deg])
    delta_lon = lon2 - lon1
    x = math.cos(lat2) * math.sin(delta_lon)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    return math.atan2(x, y)

def main():
    parser = argparse.ArgumentParser(description="Prosessoi GoPro-videon datan Street View -muotoon.")
    parser.add_argument('--video', required=True, help='Lähdevideon tiedostonimi (esim. video.mp4)')
    parser.add_argument('--interval', type=float, required=True, help='Kuvien otantaväli sekunteina')
    parser.add_argument('--outputdir', required=True, help='Hakemisto, johon tulokset tallennetaan')
    args = parser.parse_args()

    video_basename = os.path.splitext(args.video)[0]
    gps_csv_file = f"{video_basename}-GPS5.csv"
    frames_dir = os.path.join(args.outputdir, 'frames')

    # --- GPS-DATAN LUKU ---
    gps_points = []
    try:
        with open(gps_csv_file, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    dt = datetime.fromisoformat(row["date"].replace("Z", "+00:00"))
                    gps_points.append({
                        "date": dt,
                        "lat": float(row["GPS (Lat.) [deg]"]),
                        "lon": float(row["GPS (Long.) [deg]"]),
                    })
                except (ValueError, KeyError):
                    continue # Ohitetaan virheelliset rivit hiljaa
    except FileNotFoundError:
        print(f"VIRHE: GPS-tiedostoa '{gps_csv_file}' ei löytynyt.")
        exit(1)

    if not gps_points:
        print("VIRHE: GPS-dataa ei löytynyt tiedostosta.")
        exit(1)

    # --- SYNKRONOINTI ---
    date_times = [p['date'] for p in gps_points]
    diffs = [(date_times[i+1] - date_times[i]).total_seconds() for i in range(len(date_times)-1)]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0.1
    gps_step = max(1, round(args.interval / avg_diff)) if avg_diff > 0 else 20

    image_files = sorted(glob.glob(os.path.join(frames_dir, '*.jpg')))
    if not image_files:
        print("VIRHE: Yhtään kuvaa ei löytynyt kansiosta. Varmista, että FFmpeg toimi oikein.")
        exit(1)

    max_items = min(len(image_files), len(gps_points) // gps_step)
    image_files = image_files[:max_items]

    synced_data = []
    for i, image_path in enumerate(image_files):
        gps_index = i * gps_step
        if gps_index < len(gps_points):
            synced_data.append({
                "image": os.path.basename(image_path),
                "lat": gps_points[gps_index]["lat"],
                "lon": gps_points[gps_index]["lon"],
            })

    # --- YAW-LASKENTA ---
    final_data = []
    for i, point in enumerate(synced_data):
        yaw = 0.0
        if i > 0:
            prev_point = synced_data[i-1]
            yaw = calculate_bearing(prev_point['lat'], prev_point['lon'], point['lat'], point['lon'])
        
        final_data.append({**point, "yaw": yaw})

    # --- TALLENNUS ---
    output_json_path = os.path.join(args.outputdir, 'data.json')
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2)

    print(f"Prosessointi valmis. {len(final_data)} kuvaa tallennettu tiedostoon {output_json_path}")

if __name__ == "__main__":
    from datetime import datetime
    main()
    