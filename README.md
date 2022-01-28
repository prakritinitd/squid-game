# SQUID GAME

The Online Squid Game where there were 4 rounds, out of which 2 were On the website and two rounds were on Google Meet.

Making the website is one thing and making it sort of unhackable was the other aspect. Hopefully no one even tried to do that.
Seasoned developers like me will click on `CTRL + U` key or may be `F12` key to open the developer console, if the user does this then automatically i will get that the user is a cheater and with that info that player will be disqualified !. Round 1 is all about api's for every action there is an api, and Round 2 is unhackable in every aspect.

### Info about the rounds:
We wanted to keep the rounds secret as this will increase the excitement of the players. So the players dont know what will happen in any round but we told them the rounds will be similiar to the webseries Squid Game. And before starting the game we arranged a meet where participants came to see how to play, ask doubts about the game and report any trouble they are facing.
So let's start :
- Round 1 `Green Light Red Light` : Here the participants have to move their head and cross some distance when the doll is not watching over them. If the participant moves too much, he/she will die. We gave the participants necessary instructions that you have to be in well lit conditions and all. if a palyer tries to open the developers console an api request will be sent to the server that the player is trying to cheat. This round uses   
  - **Three JS** for movement of the doll.
  - **Pico JS** for face detection of the player.

    So this was the plan, the players will get 2 minutes to cover the distance of 65 meters, which is ofcourse too easy considering the fact that i once completed 100m in 30s. I love this round,honestly.

    I had very less time and was working more on the backend part, so thanks to [Louis Hoebregts](https://codepen.io/Mamboleoo), he already made this game and uploaded it open source on Codepen. I modified the bg color to black(Black instills fear) and some other functions to the JS file so that when the user click on start button he goes to full screen. Some players faced some problem there was a guy who was playing from his laptop and he had Configured OBS Studio to work as his camera, sort of so he was not able to play. And others were the ones who Were using the default browser on their android which is extra secure (This dumb app wont let the users turn on thier camera for any website). Others were just bluffing that this happend that happend but they cant fool the guy who has played the same game 100s of times.


- Round 2 `Paper Candy` : Here the participant will be assigned a candy shape randomly out of the following four shapes `Heart`, `Crescent`, `Umbrella` and `Star`. Yeah i know some of these shapes were not there in the actual squid game, there were `Circle` and `Triangle` too, but those two are too easy to make and instead of making the other two shapes easier(viz. by removing `Umbrella and Star`) and `Bihaan` gave this awesome idea of making it difficult for everyone by introducing new shapes.

- Round 3 `Tug of Knowledge` : This is where the Theme of our Club was introduced obviously we cant conduct tug of war in online mode, but we have this idea that all the qualified members will be given a team(We didnt give them the chance to choose their Team because most of the Participants were from first year and it had been hardly 2 months of them joining the college so they didnt know each other yet, and we didnt want anyone to feel left out) and we will ask them questions regarding nature. This round was hell of an interactive round, everyone has to turn on their camera and only their group leaders will answer the question other members will text in their WhatsApp group.

All the teams were named on the Name of some popular Environmentalists, There were 6 Teams having an average of 10-11 members. The team names were :

1. Team Bahuguna.
2. Team Greta.
3. Team Sumaira.
4. Team Leonardo.
5. Team Carson.
6. Team Mendes.

- Round 4  `The final round` : Only 20 people qualified for the previous round. As this is the final round only one guy would survive and win this game. The game is as follows, Some pop music will be played in the background and while the music is played players have to arrange the Alphabets shown on their screen in correct alphabetical order and send the correct word only after the music that is being played is stopped. The one who sends the correct word in Google Meet chat box (Extra layer of Transparency)
  - Before the music has ended, or
  - Is the last one to send the correct word, or
  - Has sent a incorrect word is eliminated.

Trust me this was so breathtaking for the players, i mean if you cant arrange the alphabets correctly you lose, if you are last one to send it you lose, if you sent the message before the music has ended you lose, with all these rules and stress to not to lose there's a song playing in the background. This time the players (1st year students of Batch 2021-2025) were so good that even with so much stress they were able to solve the unarranged letter on time.

Finally Player `Altaf Hussain` won.

### Stats about the event :
- 300+ Participants registered for this game.
- 280+ have played the first round.
- 120+ people qualified for round 2.
- 74 people qualified for round 3.
- 19 people qualified for the last round that is round 4.
- Many participants came from other colleges too they mentioned how much they liked playing this game.

As far as i know no other club has shown such level of creativity in their events, because until now and even now the scenario is, If there is an online event chances are 90% of the time it will be a quiz. This event which we conducted was diffrent, this was an actual game and the theme was of Squid Game. We were preparing for this event for last one month and the event was quite a success. 

### Deployment was done on AWS at the subdomain of prakriti.in.net

This was the toughest part because i was doing this for the first time it took me almost 48hours to full deploy and test the website, however i learnt a lot during these 48 hours.

I used a t2 micro instance on AWS, with 1 Gb RAM and 25 Gb SSD storage, which ran smoothly during the event there was no timeout observed.

I had to configure Gunicorn Nginx and Supervisor to run my App. I was already familiar with linux commands as i have termux in my phone. That part was easy the harder part was how to configure the Instance such that it gets the SSL cetficate and runs on the subdomain of Prakriti. And once i compelete this i got a link to check for the SSL certificate, i clicked on the link and i got a good report that everything is fine with my website and it is hosted on my subdomain but when i tried going to [Link](https://squidgame.prakriti.in.net) nothing showed up, the website can be opened in Incognito mode nd was reachable in Brave Browser and phone and here i was thinking that it didnt work. I used glass morphism and made Animated modals whereever i found it necessary.

Here are some self explanatory pictures for the event.


![](./Documentation/1.png)
![](./Documentation/2.png)
![](./Documentation/3.png)
![](./Documentation/4.png)
![](./Documentation/5.png)
![](./Documentation/6.png)
![](./Documentation/7.png)
![](./Documentation/8.png)
![](./Documentation/9.png)
![](./Documentation/10.png)
![](./Documentation/11.png)
![](./Documentation/12.png)
![](./Documentation/13.png)
![](./Documentation/14.png)
![](./Documentation/15.png)
![](./Documentation/16.png)
![](./Documentation/17.png)
![](./Documentation/18.png)
![](./Documentation/19.png)
## Participants liked the flipping card and sent it in the group. Here is the list of Player cards that we got
<p align="center">
<img align="center" src="./Documentation/20.jpeg" />
</p>