from layout.time_viz.time_viz_callbacks import update_cumulative_count
from layout.total_capacity.total_capacity_callbacks import update_capacity
from layout.models.models_callbacks import update_models
from layout.map.map_callbacks import update_map
from layout.layout import layout
from app import app, server


app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, host="localhost")