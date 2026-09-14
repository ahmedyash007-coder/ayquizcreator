# cat > /tmp/test_kivy.py <<'EOF'
from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="KIVY TEST OK")

TestApp().run()
EOF