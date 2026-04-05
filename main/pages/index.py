import reflex as rx

from main.layouts.dashboard_layout import dashboard_layout

@rx.page("/index", title="Dashboard - Reflex")
def index() -> rx.Component:
    return dashboard_layout(
        rx.box(
            rx.heading("Dashboard", size="8", weight="bold"),
            rx.text(
                "Welcome to your dashboard! Here you can find an overview of your projects, analytics, and messages.",
                size="4",
                color="gray",
            ),
            spacing="0",
            # spacing="1.5rem",
        )
    )