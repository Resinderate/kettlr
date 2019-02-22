# kettlr
Voice activated kettle with google home and raspberry pi.

### Problem
I wanted to be able to be able turn on the kettle in my kitchen remotely, so from other rooms in the flat or when outside the house.

### High Level Solution Components
- A raspberry pi + servo.
- Lego
- Flask web server.
- Port forwarding + DynamicDNS
- Custom IFTTT Applet.

### Approach
##### Raspberry pi
I used a Raspberry Pi 3 Model B+ and purchased a [hardware starter kit which included a servo motor](https://www.amazon.co.uk/gp/product/B01G5K0E0Y/ref=ppx_yo_dt_b_asin_title_o01_s02?ie=UTF8&psc=1). In Python I then built a class to interact with the servo and perform a simple forward and backward motion.

##### Lego
Now that I had the servo doing it's job I needed to mount it next to my kettle. I tested it by hand initially, and then constructed a small enclosure for the servo out of lego. This let me line it up via trial and error. The servo is quite strong, but when the arm presses down on the kettle ON switch, the enclosure moved away before activating the switch. To solve this I placed the enclosure on a green baseplate, and sat the entire kettle on top of it. This let the weight of the kettle itself keep the enclosure in place.

##### Flask
At this point it was possible to activate the kettle by running my program directly on the pi. The next step was to open this up to other services. I created a minimal flask app which would run on the pi, accept a request, and in turn use the "KettleRobot" to turn on the kettle locally. I used nginx to route requests to the correct app and supervisor to manage the app lifecycle. Supervisor is configured to start when the pi starts allowing for easy headless operation. By using supervisor I can also restart the service remotely with a simple SSH call, allowing for a CI/CD process to push updates using travisCI when I merge in updates on github.

##### Port forwarding + DynamicDNS
I have a basic residential internet connection. I configured my pi to use a fixed IP address on the network, and then set up port forwarding to send any incomming requests to the pi. As it's a residential connection I don't have a fixed IP address which poses a problem for external apps knowing where to look. To solve this I utilized a DynamicDNS service called DuckDNS. This sets up a fixed DNS entry which will then forward to whichever IP I specify to be my current address in use by my ISP. I set up an hourly CRON on the pi to ping DuckDNS and update it with the current IP in use.

I additionally mapped a subdomain on my own personal domain for ease of use, so ultimately I can use kettle.mur-phy.com to reach the pi.

##### Custom IFTTT Applet
Now I have the ability to send a simple HTTP request which will in turn activate my kettle! The next step is to do so via my Google Home Assistant. Using IFTTT I can set up an Applet with a trigger and action. The trigger in this case is me speaking to Google Home with a specific phrase. The action is simply sending the correctly formatted request. This completes the chain, and I can now either call out to my Google Home Mini when in range, or alternatively through Google Assistant on my Android phone. The same is set up on my SO's phone so both of us can do the same.

### Demo
[The end result looks like this!](https://www.youtube.com/watch?v=NtcqWjXcCE0)
