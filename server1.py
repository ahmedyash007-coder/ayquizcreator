

from flask import Flask, request, jsonify, send_file
import os
import subprocess
import shutil
from PIL import Image, ImageDraw
import numpy as np



from PIL import (
    Image as PILImage,
    ImageDraw,
    ImageFilter,
    ImageFont
)


from textwrap import wrap
import textwrap

import random
import threading
import time
import os
import requests
import shutil
import math
import uuid
import os
import subprocess
from PIL import Image, ImageDraw, ImageFont
from PIL import Image as PILImage
import colorsys
from threading import Thread
import uuid
FONT_PATH = os.path.join(
    os.path.dirname(__file__),
    "fonts",
    "Roboto.ttf"
)

global stars
global matrix_drops
galaxy_bg = None
stars = None
matrix_drops = None
fire_bg = None

APP_DURATION = 10  












app = Flask(__name__)


        
 

jobs = {}












def box(img, x1, y1, x2, y2, color=(255,255,255), text="",font=None):

  

    h, w = img.shape[:2]


    if isinstance(color, str):
        color = (255,255,255)

    if len(color) >= 3:
        r = min(255, int(color[0]))
        g = min(255, int(color[1]))
        b = min(255, int(color[2]))
    else:
        r, g, b = 255, 255, 255

    # background fill
    img[y1:y2, x1:x2] = (
        int(r * 0.25),
        int(g * 0.25),
        int(b * 0.25)
    )

    # border
    img[y1:y1+3, x1:x2] = (r, g, b)
    img[y2-3:y2, x1:x2] = (r, g, b)
    img[y1:y2, x1:x1+3] = (r, g, b)
    img[y1:y2, x2-3:x2] = (r, g, b)

    pil_img = PILImage.fromarray(img)
    draw = ImageDraw.Draw(pil_img)

   


    padding = 25

    if font is None:

        font = get_fit_font(
            draw,
            text,
            (x2 - x1) - padding * 2,
            (y2 - y1) - padding * 2
        )

        




    

  
    bbox = draw.multiline_textbbox(
        (0,0),
        text,
        font=font
    )

    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    tx = x1 + ((x2 - x1) - text_w) // 2
    ty = y1 + ((y2 - y1) - text_h) // 2

    draw.multiline_text(
        (tx, ty),
        text,
        fill=(255,255,255),
        font=font,
        align="center"
    )




    img[:] = np.array(pil_img)    

    return img


def draw_quiz(img, q, opts, correct):

    h, w = img.shape[:2]

    

    box_w = int(w * 0.80)     
    box_h = int(h * 0.11)    
    gap = int(h * 0.02)
    q_h = int(h * 0.18)

    total_h = q_h + (box_h + gap) * 4

    start_y = (h - total_h) // 2

    qx1 = (w - box_w) // 2
    qx2 = qx1 + box_w

    qy2 = start_y + q_h

    question_text = "\n".join(
        textwrap.wrap("Q: " + str(q), width=25)
    )


    box(
        img,
        qx1,
        start_y,
        qx2,
        qy2,
        (255, 223, 0 ,1),
        question_text
    )

    colors = [
      
        (82, 32, 129,1),
        (82, 32, 129,1),
        (82, 32, 129,1),
        (82, 32, 129,1)
    ]

    labels = ["A","B","C","D"]

    for i in range(4):

        y1 = qy2 + 20 + i * (box_h + gap)
        y2 = y1 + box_h

        opt = "\n".join(
            textwrap.wrap(
                f"{labels[i]}) {opts[i]}",
                width=28
            )
        )

        box(
            img,
            qx1,
            y1,
            qx2,
            y2,
            colors[i],
            opt
        )








def get_fit_font(draw, text, max_width, max_height):

    size = 100

    while size > 20:

        font = ImageFont.truetype(FONT_PATH, size)

        bbox = draw.multiline_textbbox((0,0), text, font=font)

        w = bbox[2]-bbox[0]
        h = bbox[3]-bbox[1]

        if w <= max_width and h <= max_height:
            return font

        size -= 2

    return ImageFont.truetype(FONT_PATH,20)






def get_frame_size(frame_size):

    if frame_size == "youtube_shorts":
        return 1080, 1920

    elif frame_size == "tiktok":
        return 1080, 1920

    elif frame_size == "square":
        return 1080, 1080

    elif frame_size == "wide":
        return 1920, 1080

    else:
        return 1080, 1920



def draw_frame(draw, frame_style, w, h):


    if frame_style == "clean":

        draw.rounded_rectangle(
            [(20,20),(w-20,h-20)],
            radius=25,
            outline=(255,255,255),
            width=6
        )


    elif frame_style == "tiktok":

        draw.rounded_rectangle(
            [(15,15),(w-15,h-15)],
            radius=40,
            outline=(255,0,120),
            width=10
        )

        draw.rounded_rectangle(
            [(30,30),(w-30,h-30)],
            radius=40,
            outline=(0,255,255),
            width=5
        )


    elif frame_style == "youtube":

        draw.rounded_rectangle(
            [(20,20),(w-20,h-20)],
            radius=20,
            outline=(255,0,0),
            width=10
        )


    elif frame_style == "gold":

        draw.rounded_rectangle(
            [(20,20),(w-20,h-20)],
            radius=30,
            outline=(255,215,0),
            width=10
        )

 
    elif frame_style == "neon":

        draw.rounded_rectangle(
            [(15,15),(w-15,h-15)],
            radius=40,
            outline=(0,255,255),
            width=10
        )

        draw.rounded_rectangle(
            [(30,30),(w-30,h-30)],
            radius=40,
            outline=(255,0,255),
            width=5
        )

    elif frame_style == "gaming":

        draw.rectangle(
            [(20,20),(w-20,h-20)],
            outline=(0,255,0),
            width=8
        )

        draw.rectangle(
            [(40,40),(w-40,h-40)],
            outline=(0,150,255),
            width=4
        )


    elif frame_style == "royal":

        draw.rounded_rectangle(
            [(20,20),(w-20,h-20)],
            radius=50,
            outline=(180,120,255),
            width=12
        )

    else:

        draw.rounded_rectangle(
            [(20,20),(w-20,h-20)],
            radius=25,
            outline=(255,255,255),
            width=5
        )










def make_frame(q, opts, correct,frame_size,bg_mode):

    def frame(t):
        print("CURRENT BG:", bg_mode) 
        global stars
        global matrix_drops
        
        print("FRAME SIZE VALUE =", frame_size)

        w, h = get_frame_size(frame_size)   # ✔️ YAHAN HO GA
    
        print("WIDTH =", w)
        print("HEIGHT =", h)        
        img = np.zeros((h, w, 3), dtype=np.uint8)
        img[:] = (0, 0, 0)



        if bg_mode == "simple":


           img = np.zeros((h, w, 3), dtype=np.uint8)

   
           img[:] = (0, 180, 0)

           img = (img * 0.95 + 20).astype(np.uint8)
       





         
        elif bg_mode == "galaxy":

            global galaxy_bg, stars



            if galaxy_bg is None:

                galaxy_bg = np.zeros((h, w, 3), dtype=np.uint8)

              
                galaxy_bg[:] = (8, 0, 32)
                cx = w // 2
                cy = h // 2
                radius = int(min(w, h) * 0.42)

                for yy in range(max(0, cy-radius), min(h, cy+radius)):
                    for xx in range(max(0, cx-radius), min(w, cx+radius)):

                        dx = xx - cx
                        dy = yy - cy

                        dist = (dx*dx + dy*dy) ** 0.5

                        if dist < radius:

                            factor = 1 - dist / radius

                            galaxy_bg[yy, xx][0] = min(
                                255,
                                galaxy_bg[yy, xx][0] + int(45 * factor)
                            )

                            galaxy_bg[yy, xx][1] = min(
                                255,
                                galaxy_bg[yy, xx][1] + int(6 * factor)
                            )

                            galaxy_bg[yy, xx][2] = min(
                                255,
                                galaxy_bg[yy, xx][2] + int(95 * factor)
                            )

            img = galaxy_bg.copy()


            if stars is None:

                stars = []

                for _ in range(140):

                    stars.append({

                        "x": random.randint(0, w-1),

                        "y": random.randint(0, h-1),

                        "speed": random.uniform(0.25, 0.8),

                        "size": random.choice([
                            3,3,
                            4,4,
                            5,5,
                            6
                        ]),

                        "brightness": random.randint(210,255),

                        "twinkle": random.uniform(0.94,1.0)

                    })


            for s in stars:

                s["y"] += s["speed"]

                if s["y"] >= h:

                    s["y"] = 0

                    s["x"] = random.randint(0, w-1)

                brightness = int(
                    s["brightness"] * s["twinkle"]
                )

                x = int(s["x"])
                y = int(s["y"])
                size = s["size"]

                for dx in range(-size, size+1):

                    for dy in range(-size, size+1):

                        nx = x + dx
                        ny = y + dy

                        if 0 <= nx < w and 0 <= ny < h:

                            dist = dx*dx + dy*dy

                            if dist <= size*size:

                                fade = 1 - (
                                    dist /
                                    (size*size + 1)
                                )

                                b = int(brightness * fade)

                                img[ny, nx] = (
                                    b,
                                    b,
                                    255
                                )












        elif bg_mode == "matrix":

            img = np.zeros((h, w, 3), dtype=np.uint8)
            img[:] = (5, 8, 5)

            letters = "01"

            if matrix_drops is None:

                matrix_drops = []

                for i in range(180):

                    matrix_drops.append({
                        "x": random.randint(0, w - 1),
                        "y": random.randint(-h, 0),
                        "speed": random.uniform(2, 6),
                        "char": random.choice(letters)
                    })

            for d in matrix_drops:

                d["y"] += d["speed"]

                if d["y"] > h:
                    d["y"] = random.randint(-50, 0)
                    d["x"] = random.randint(0, w - 1)
                    d["speed"] = random.uniform(2, 6)

                if random.random() < 0.02:
                    d["char"] = random.choice(letters)

                x = int(d["x"])
                y = int(d["y"])

                if 0 <= x < w and 0 <= y < h:

                    img[y, x] = (0, 255, 120)

                    if x + 1 < w and y + 1 < h:
                        img[y + 1, x + 1] = (0, 120, 255)

                    if y + 2 < h:
                        img[y + 2, x] = (0, 180, 80)        







        elif bg_mode == "fire":

            img = np.zeros((h, w, 3), dtype=np.uint8)

   
            img[:] = (5, 5, 15)

 
            for i in range(35):

                flame_x = random.randint(0, w)

   
                flame_y = random.randint(int(h * 0.55), h)

                flame_y -= int((t * 8 + i * 15) % 250)

                radius = random.randint(30, 90)

                fire_colors = [
                    (0, 80, 255),    # orange
                    (0, 140, 255),   # light orange
                    (0, 200, 255),   # yellow
                    (40, 255, 255)   # bright yellow
                ]

                color = random.choice(fire_colors)

 
                for dy in range(-radius, radius):

                    yy = flame_y + dy

                    if yy < 0 or yy >= h:
                        continue

                    for dx in range(-radius // 2, radius // 2):

                        xx = flame_x + dx

                        if xx < 0 or xx >= w:
                            continue

                        dist = (dx * dx) / 1.8 + (dy * dy)

                        if dist < radius * radius:

                            fade = 1 - dist / (radius * radius)

                            img[yy, xx][0] = min(
                                255,
                                img[yy, xx][0] + int(color[0] * fade * 0.45)
                            )

                            img[yy, xx][1] = min(
                                255,
                                img[yy, xx][1] + int(color[1] * fade * 0.45)
                            )

                            img[yy, xx][2] = min(
                                255,
                                img[yy, xx][2] + int(color[2] * fade * 0.45)
                            )

  
            img = np.clip(img * 1.08, 0, 255).astype(np.uint8)        






        elif bg_mode == "neon":

            img = np.zeros((h, w, 3), dtype=np.uint8)


            img[:] = (18, 10, 35)

            colors = [
                (255, 0, 180),
                (0, 255, 255),
                (140, 0, 255),
                (0, 255, 120),
                (255, 220, 0)
            ]

            for i in range(18):

                x = random.randint(0, w)
                y = random.randint(0, h)

                radius = random.randint(25, 70)

                color = random.choice(colors)

                for dy in range(-radius, radius):

                    yy = y + dy

                    if yy < 0 or yy >= h:
                        continue

                    for dx in range(-radius, radius):

                        xx = x + dx

                        if xx < 0 or xx >= w:
                            continue

                        d = dx * dx + dy * dy

                        if d < radius * radius:

                            fade = 1 - d / (radius * radius)

                            img[yy, xx][0] = min(
                                255,
                                img[yy, xx][0] + int(color[0] * fade * 0.25)
                            )

                            img[yy, xx][1] = min(
                                255,
                                img[yy, xx][1] + int(color[1] * fade * 0.25)
                            )

                            img[yy, xx][2] = min(
                                255,
                                img[yy, xx][2] + int(color[2] * fade * 0.25)
                            )

  
            offset = int((t * 4) % w)

            img = np.roll(img, offset, axis=1)        






        elif bg_mode == "cyberpunk":

            img = np.zeros((h, w, 3), dtype=np.uint8)


            img[:] = (25, 10, 35)


            spacing = 70

            offset = int((t * 2) % spacing)

            for y in range(-spacing, h + spacing, spacing):

                yy = y + offset

                if 0 <= yy < h:

                    img[yy:yy+2, :] = (255, 40, 180)

                    if yy + 2 < h:
                        img[yy+2:yy+4, :] = (120, 20, 80)


            spacing = 70

            offset = int((t * 2) % spacing)

            for x in range(-spacing, w + spacing, spacing):

                xx = x + offset

                if 0 <= xx < w:

                    img[:, xx:xx+2] = (0, 255, 255)

                    if xx + 2 < w:
                        img[:, xx+2:xx+4] = (0, 120, 120)


            scan = int((t * 8) % h)

            img[max(0, scan-2):min(h, scan+2), :] = (255, 80, 220)

 
            for i in range(12):

                x = (i * 170 + t * 5) % w
                y = (i * 130) % h

                x = int(x)
                y = int(y)

                img[max(0,y-2):min(h,y+2),
                    max(0,x-2):min(w,x+2)] = (255,255,255)

 
            img = (img * 0.96).astype(np.uint8)        





        FPS = 24

        duration = APP_DURATION

        COUNTDOWN_TIME = 3
        ANSWER_TIME = 2

        QUESTION_TIME = duration - COUNTDOWN_TIME - ANSWER_TIME

        QUESTION_FRAMES = QUESTION_TIME * FPS
        COUNTDOWN_FRAMES = COUNTDOWN_TIME * FPS
        ANSWER_FRAMES = ANSWER_TIME * FPS

        TOTAL_FRAMES = QUESTION_FRAMES + COUNTDOWN_FRAMES + ANSWER_FRAMES


         

        if t < QUESTION_FRAMES:

            draw_quiz(img, q, opts, correct)


        elif t < QUESTION_FRAMES + COUNTDOWN_FRAMES:

            draw_quiz(img, q, opts, correct)

   
            remaining = int(
                 (QUESTION_FRAMES + COUNTDOWN_FRAMES - t) / FPS
             )

            text = str(remaining) if remaining > 0 else "GO!"

            center = (w // 2, h // 2)

   
            scale = 1 + 0.08 * np.sin((t / FPS) * 2 * np.pi)

            pil_img = PILImage.fromarray(img)
            draw = ImageDraw.Draw(pil_img)

            radius = round(240 * scale)

            draw.ellipse(
        (
            center[0] - radius,
            center[1] - radius,
            center[0] + radius,
            center[1] + radius
        ),
                fill=(255, 255, 0)
    )



            draw = ImageDraw.Draw(pil_img)

       

            try:

                font = ImageFont.truetype(
                    FONT_PATH,
                    320
                )
                
                
                print("COUNTDOWN FONT LOADED")
            except Exception as e:
                print("COUNTDOWN FONT ERROR:", e)
                font = ImageFont.load_default()            





    


            bbox = draw.textbbox((0, 0), text, font=font)

            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            x = (w - text_w) // 2 - bbox[0]
            y = (h - text_h) // 2 - bbox[1]

            draw.text(
                (x + 6, y + 6),
                text,
                fill=(0, 0, 0),
                font=font
            )


            draw.text(
                (x, y),
                text,
                fill=(255, 215, 0),
                font=font
            )












            img = np.array(pil_img)

        else:

            draw_quiz(img, q, opts, correct)

            pil_img = PILImage.fromarray(img)

            overlay = PILImage.new(
        "RGB",
        (w, h),
        (0, 0, 0)
    )

            overlay_draw = ImageDraw.Draw(overlay)

            overlay_draw.rectangle(
        (
            w // 2 - 350,
            h // 2 - 120,
            w // 2 + 350,
            h // 2 + 120
        ),
                fill=(48, 25, 52)
    )

            pil_img = PILImage.blend(
        pil_img,
        overlay,
        0.25
    )

            pil_img = pil_img.filter(
                ImageFilter.GaussianBlur(radius=2)
    )

            draw = ImageDraw.Draw(pil_img)



            text = "ANSWER: " + correct

            padding = 80

            font = get_fit_font(
                draw,
                text,
                w - padding * 2,
                300
            )


            bbox = draw.textbbox((0, 0), text, font=font)

            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            x = (w - text_w) // 2
            y = (h - text_h) // 2            






         



            glow = PILImage.new(
        "RGB",
        (w, h),
        (0, 0, 0)
    )

            glow_draw = ImageDraw.Draw(glow)

            glow_draw.ellipse(
        (
            w // 2 - 220,
            h // 2 - 220,
            w // 2 + 220,
            h // 2 + 220
        ),
                fill=(0, 180, 255)
    )

            glow = glow.filter(
                ImageFilter.GaussianBlur(radius=35)
    )

            pil_img = PILImage.blend(
        pil_img,
        glow,
        0.18
    )

            draw = ImageDraw.Draw(pil_img)



            draw.text(
        (x, y + 6),
        text,
        fill=(0, 0, 0),
        font=font
    )

            draw.text(
        (x, y),
        text,
        fill=(0, 255, 255),
        font=font
    )

            draw.text(
        (x, y),
        text,
        fill=(255, 255, 255),
        font=font
    )

            img = np.array(pil_img)







        return img

    return frame
















def generate_video_job(job_id, data, base_url):

    jobs[job_id] = {
        "status": "processing"
    }

    print("BACKGROUND JOB STARTED:", job_id)

    
     

    


    
    quiz_data = data.get("quiz", [])
    frame_style = data.get("frame_style", "clean")
 
    bg_mode = data.get("bg", "dark")
    print("BG MODE =", bg_mode)
    frame_size = data.get("frame_size", "tiktok")
    fps = 24

  

    APP_DURATION = int(data.get("duration", 10))

    TOTAL_FRAMES = APP_DURATION * fps    


    frame_no = 0

    w, h = get_frame_size(frame_size)


    process = subprocess.Popen(
    [
        "ffmpeg",
        "-y",
        "-f", "rawvideo",
        "-pix_fmt", "rgb24",
        "-s", f"{w}x{h}",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "output.mp4"
    ],
        stdin=subprocess.PIPE
    )  

    APP_DURATION = int(data.get("duration", 10))
    APP_DURATION = int(APP_DURATION)

    print("APP_DURATION =", APP_DURATION)
    print("TOTAL QUESTIONS:", len(quiz_data))
    print("FRAME STYLE:", frame_style)
    print("BG MODE:", bg_mode)
    print("FRAME SIZE:", frame_size)
    print(quiz_data)
    print("APP_DURATION =", APP_DURATION)
    print("TOTAL_FRAMES =", TOTAL_FRAMES)
    # =========================


    for q in quiz_data:
      
        question = q["q"]
        options = q["options"]
        correct = q.get("correct")

   
        generator = make_frame(
              question,
              options,
              correct,
              frame_size,
              bg_mode
             )
       

        

        for t in range(TOTAL_FRAMES):

            start = time.time()

            img_array = generator(t)

            end = time.time()

            print(
                "Frame",
                t,
                "Generation Time =",
                round(end - start, 3),
                "seconds"
            )

            if img_array is None:
                continue

            process.stdin.write(
                img_array.astype("uint8").tobytes()
            )

            frame_no += 1

            if frame_no % 100 == 0:
                print("Frames sent:", frame_no)    













    
       



   





    if frame_no == 0:
        return jsonify({
            "status": "error",
            "message": "No Video frames generated"
        }), 400

    print("TOTAL FRAMES SENT TO FFMPEG:", frame_no)


    
    
    process.stdin.close()

    return_code = process.wait()

    print("FFmpeg finished")
    print("FFMPEG RETURN CODE:", return_code)


    if return_code != 0:
        jobs[job_id] = {
          "status": "error",
          "message": "FFmpeg failed"
        }
        return




    jobs[job_id] = {
        "status": "done",
       
        "video_url": base_url + "/output.mp4"
    }

    print("BACKGROUND JOB FINISHED:", job_id)










@app.route("/generate", methods=["POST"])
def generate():





    print("===== GENERATE REQUEST RECEIVED =====")

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "status": "error",
            "message": "No JSON received"
        }), 400


    job_id = str(uuid.uuid4())

    print("JOB ID =", job_id)
    base_url = request.host_url.rstrip("/")


    Thread(
        target=generate_video_job,
        args=(job_id, data, base_url)
    ).start()


    return jsonify({
        "status": "started",
        "job_id": job_id
    })



@app.route("/output.mp4")
def output_video():

    return send_file(
        "output.mp4",
        mimetype="video/mp4"
    )





@app.route("/status/<job_id>")
def status(job_id):

    if job_id not in jobs:
        return jsonify({
            "status": "not_found"
        })

    return jsonify(
        jobs[job_id]
    )








if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



