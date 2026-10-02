[app]

title = AY QUIZS
package.name = ayquizcreator
package.domain = org.ay

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,mp3,ttf,json,txt

version = 1.0

requirements = python3,kivy,pillow,numpy,requests,pyrebase4

orientation = portrait
fullscreen = 0

icon.filename = ahmed_logo13.png

android.permissions = INTERNET

android.api = 35
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a


[buildozer]

log_level = 2
warn_on_root = 1
