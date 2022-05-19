from EduBot import WheelBot


robot = WheelBot(trigPin=[12,5],echoPin=[15,4],in1=18,in2=19,in3=20,in4=21)
robot.stop()


while True:
    
    dist=robot.distance()
    if abs(dist[0]-dist[1])<5: #insignificant distance
        robot.forward()
    elif dist[0]>dist[1]: #ione sensor clsoer than othre
        robot.right(delay=0.5)
        robot.forward()
    else: #other sensor closer than sensor
        robot.left(delay=0.5)
        robot.forward()
    
    utime.sleep(0.5)
