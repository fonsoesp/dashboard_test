import reflex as rx
from main.components.sidebar import sidebar_bottom_profile

def dashboard_layout(content: rx.Component) -> rx.Component:
    return rx.flex(
        sidebar_bottom_profile(),
        rx.box(
            content,
            flex="1",
            padding="2rem",
            min_height="100vh",
        ),
        width="100%",
        min_height="100vh",
    )