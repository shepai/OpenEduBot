import mujoco
import mujoco.viewer
import numpy as np
import time

# Load model
model = mujoco.MjModel.from_xml_path("D:/Documents/Github/OpenEduBot/Mujoco_Simulation/robot/wheelbot.xml")
data = mujoco.MjData(model)

light_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_LIGHT, 'top_lamp')
light_pos = model.light_pos[light_id]
def get_virtual_light_intensity(data, site_name):
    # Get current world position of the sensor site
    sensor_pos = data.site(site_name).xpos
    
    # Calculate distance to the light pos we pulled from the XML
    distance = np.linalg.norm(sensor_pos - light_pos)
    
    # Simple "Intensity = 1 / Distance^2" logic
    return 1.0 / (distance**2 + 0.01)

# Launch viewer
with mujoco.viewer.launch_passive(model, data, show_left_ui=False, show_right_ui=False) as viewer:
    while viewer.is_running():
        left_val = get_virtual_light_intensity(data, 'light_sensor_left')
        right_val = get_virtual_light_intensity(data, 'light_sensor_right')
        data.ctrl[0] = right_val*-100
        data.ctrl[1] = left_val*-100
        print(f"Left Sensor: {left_val:.3f}, Right Sensor: {right_val:.3f}")
        mujoco.mj_forward(model, data)
        mujoco.mj_step(model, data)
        viewer.sync()