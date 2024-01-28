import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Define the transfer function of the system (first-order with time delay)
numerator = [1]
denominator = [5, 1]
system = ctrl.TransferFunction(numerator, denominator, dt=2)

# Define PID controller parameters
Kp = 1.0
Ki = 0.1
Kd = 0.01

# Create PID controller with the same time base as the system
pid_controller = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0], dt=2)

# Connect the system and controller
open_loop_system = ctrl.series(pid_controller, system)

# Create a closed-loop system
closed_loop_system = ctrl.feedback(open_loop_system)

# Time vector for simulation should be in steps of dt=2
time = np.arange(0, 20 + 2, 2)  # Ends at 20 seconds with steps of dt

# Step response of the closed-loop system
time, response = ctrl.step_response(closed_loop_system, time)

# Plot the step response
plt.plot(time, response, label='System Response')

# Plot the target line (for a unit step input, the target is 1)
plt.axhline(y=1, color='r', linestyle='--', label='Target')

# Add title and labels
plt.title('Step Response of PID-controlled System')
plt.xlabel('Time (seconds)')
plt.ylabel('System Response')

# Add a legend
plt.legend()

# Add grid
plt.grid(True)

# Show the plot
plt.show()