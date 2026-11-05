[app]
title = QR-генератор
package.name = qrapk
package.domain = org.dan
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy==2.3.0,qrcode,pillow
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1