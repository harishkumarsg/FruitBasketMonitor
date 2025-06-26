from scripts.yolo_detect_and_crop import detect_and_crop_fruits
from scripts.rot_segmentation import estimate_rot_percent
from scripts.report_generator import generate_report
import os
from datetime import datetime

# 📸 Input image path (your fruit basket image)
img_path = 'scripts/fruitbasket2.jpg'

# 📂 Directory to save cropped fruit images
crop_dir = 'classifier/cropped_fruits'
os.makedirs(crop_dir, exist_ok=True)

# 🧠 Detect and crop fruits using YOLO
fruit_data, annotated_path = detect_and_crop_fruits(img_path, crop_dir)

results = []
for fruit in fruit_data:
    # 🎯 Calculate rot percentage
    rot_percent = estimate_rot_percent(fruit['path'])

    # ✅ Decide type based on rot %
    if rot_percent >= 50:
        fruit_type = "rotten"
    else:
        fruit_type = "fresh"

    fruit['rot_type'] = fruit_type  # This is what gets displayed in report
    results.append(fruit)

# 📝 Generate report with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
pdf_path = f"output/reports/report_{timestamp}.pdf"
generate_report(results, annotated_path, pdf_path)

print(f"✅ Report generated: {pdf_path}")
