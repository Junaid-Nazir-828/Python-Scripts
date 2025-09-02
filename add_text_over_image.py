from PIL import Image, ImageDraw, ImageFont

# === CONFIG ===
input_file = "img.png"
output_file = "output.png"
new_text = "75%"  # Replace as needed
font_path = "arial.ttf"  # Ensure this TTF file exists
font_size = 150
text_color = (0, 255, 255)  # Neon cyan
outline_color = (0, 180, 180)
outline_radius = 8  # For glow

# === OPEN IMAGE ===
img = Image.open(input_file).convert("RGBA")
draw = ImageDraw.Draw(img)

# === FONT ===
font = ImageFont.truetype(font_path, font_size)

# === CALCULATE TEXT SIZE & CENTER POSITION ===
bbox = font.getbbox(new_text)  # returns (x0, y0, x1, y1)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]
W, H = img.size
x = (W - text_w) / 2
y = (H - text_h) / 2 - 120

# === GLOW EFFECT ===
for dx in range(-outline_radius, outline_radius + 1):
    for dy in range(-outline_radius, outline_radius + 1):
        if dx**2 + dy**2 <= outline_radius**2:
            draw.text((x + dx, y + dy), new_text, font=font, fill=outline_color)

# === MAIN TEXT ===
draw.text((x, y), new_text, font=font, fill=text_color)

# === SAVE OUTPUT ===
img.save(output_file)
print(f"Saved image as {output_file}")
