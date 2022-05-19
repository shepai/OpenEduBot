from EduBot import WheelBot


robot = WheelBot(trigPin=26,echoPin=22,in1=18,in2=19,in3=20,in4=21)
robot.stop()


while True:
    
    dist=robot.distance()
    robot.forward() #defualt move forward
    if dist<30: #turn when ruler length away from obstacle
        robot.turn()
    robot.forward() #defualt move forward
    utime.sleep(0.5)
