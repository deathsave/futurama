# Futurama-pinball

Futurama Pinball Documentation

Contents:

1. About this machine
2. Settings Menu
3. Gameplay + Modes
4. Theory of Operation
    1. Boards
    2. Power Circuit
    3. Switches + Optos (with wiring diagrams)
    4. Coils (with wiring diagrams
    5. Lights (with wiring diagrams)

1- About this Machine

This Futurama pinball machine was originally built by Evan Kizer around 2005 using salvaged parts and boards from other games and a custom playfield and cabinet; I’ve included a print-out of an archived version of his AOL website that goes into some detail about where the idea came from and how he built it.

Evan was an avid pinball collector and a Seattle local; he went to Ballard High School, class of ’83. He lived on Queen Anne Hill, 21 steps to his front door; but still managed to collect over 20 machines at his home. Although there were a few notes and hints at ideas for other games on his website, our understanding is that Futurama is the only custom pinball machine he ever built. There are a few old articles and some short video clips of his original machine online including on Make Magazine’s website, but to the best of our knowledge the machine was never “routed” or put out for play in public.

Unfortunately, Evan passed away in 2021; per his wishes he was cremated with a pinball. His collection was passed on to his family who has kept and cherished much of it. At the time he passed, Futurama was partially disassembled and not functional; his family held on to it but was unsure of what to do with it since as a custom machine, it would have been nearly impossible to fix without Evan. His family didn’t want it to just be disassembled for parts… ideally they wanted somebody who would take it on and embrace the project.

The game has been rebuilt and redesigned with P3 boards (Multimorphic) and uses the Mission Pinball Framework for the code. Currently this machine is being developed only as a homebrew project with no commercial intentions, however once the code is done we may seek approval + IP licensing to produce a commercial product if possible.

3- Gameplay and Modes

**Pizza Delivery at the Cryogenics Lab-**

Start ball 1 with a pizza delivery to the cryogenics lab. Get to the lab (loop shot from either entry), realize the delivery is a prank, and crack a cold one to toast “another lousy millennium”; this will start the new years countdown “hurry up”, if you make this shot then the short “welcome to the world of tomorrow” clip plays, and the reward is **points** as well as enabling the left outlane “suicide booth” ball save. Failing to make the hurry up ends the first delivery with no cut scene or reward, just the first few bell tones from the theme and then cut right to the meeting room at planet express HQ.

**You can also skip this mode by making a skill shot on ball one, which shows the cut scene of Fry confronting Nibbler but then choosing to let himself get frozen anyway. This skillshot rewards the ball save and points but skips the cut scene.**

**If the player drains the ball before completing the mode then their next ball will start in the planet express HQ meeting room.**

**Base Mode-**

After completing, failing, or skipping the cryogenics lab delivery in ball one, and in every ball after that, the main mode of the game starts. In this mode there are multiple scoring shots and combos as well as others that enable, activate, or build-up to other modes.

**Planet Express Ship Spinning Platter-**

Hitting the Spinning Platter builds a value that lights the mystery shot. Once the shot has been hit enough times to build the value high enough, the scoop is lit for a 2 ball “demolition derby multiball”. Value of Spinning Platter is 1 point per 120 degree rotation x the Crew Multiplier, which is increased by 1 for every crew member with a Character Level of 2 or higher, up to 9 points per 120 degree rotation with the Crew Multiplier maxed out.

**Tube Transport left ramp)-**

Shooting the left ramp plays a tube transport clip. The left ramp feeds back to the left inlane; the left inlane switch lights the HQ (right loop) shot and toggles the right orbit shot between Zapp and Mom.

**Slurm Caps-**

There are 4 star-rollover switches on the playfield, everytime a player hits one it increases their total caps collected. At the beginning of each game the machines sets a random number between 20 and 80; this number is not knowable to the player but once they reach it, “Slurm Factory Mode” is lit (delivery shot).

**Good News!/Delivery Shot(scoop)-**

Hitting the planet express ship spinning platter enough times (50 full rotations) lights the scoop (a different color than when a delivery is ready) to collect “Good News!”, aka the mystery award, including:

\-“Pimparoo” **points**

**\-“**Emporer Nimbala” (Mummy Jerky)

\-“Blurnsball” multiball

\-1 Slurm Cap\*

\-1/4 tank of dark matter\*

\-full tank of dark matter

\-left outlane ball save

\-“7-leaf clover” (7x multiplier for 77 seconds or end of ball)

\-collect 1 head in a jar

\-300 big boys **points**

\-gender swap (30 seconds of reversed flippers)

\-“Robanakuh” (30 second ball save)

Except for awards marked with \* , each Good News! Award can only be received once per game per player

**Old New York (left loop)-**

Left loop shot is lit for a short time after right inlane rollover switch is hit. Building up enough Old New York shots (per player across the whole game) progresses through the “old new York” tiers, as follows:

1. Fry remembers 20<sup>th</sup> century New York – 1 lit shot
2. Rescue Nibbler (hurry-up, collect for ½ tank dark matter) – 3 lit shots
3. Leila’s parents – 5 lit shots
4. Mutant Fry – 8 lit shots
5. Sewer Surfing – 12 lit shots
6. Mutant Uprising – 18 lit shots
7. Mom’s gene cure lab – 25 lit shots

Each time a player reaches a new tier, the ball locks in the loop and the display plays a short cutscene and the value of the left loop shot (lit or unlit) increases by 1x per tier.

**Planet Express HQ (right loop)-**

Hitting the left ramp lights the Planet Express HQ shot temporarily, making the shot as a combo after hitting the left ramp increases a value that advances the shot through tiers that increase the value of the right loop shot (lit or not) and plays a brief clip everytime the player advances to the next tier:

1. “I’m your uncle fry” + 5 Fry XP
2. “Lengths of wire, intergalactic space ship” +5 Professor XP
3. Hermes talking about “pest problem” (Owls)
4. …
5. Head in a jar
6. Hubert (extra ball)
7. “owl exterminators” (Mom qualifier)

**Lrr (pop bumper)-**

Hitting the pop bumper briefly plays the hypnotoad sound and builds a value that starts “hypnotoad wizard mode” when it is built enough (total hits by all players, only 1 player can activate mode per game, value to activate is very high)

**Zapp Brannigan (right orbit)-**

Advance Zapp Brannigan by hitting the right orbit. Each tier raises the value of the shot across modes, and some tiers trigger a hurry-up jackpot.

1. “the Zapp Brannigan” (hurry up)
2. Zapp and Kipp
3. Zapp talking about this uniform
4. Zapp tries to be seductive (hurry up)
5. Capitan of a ship (the titanic episode)
6. Zapp being a jerk at a bar
7. Zapp and Nixon (hurry up, success awards Nixon head in a jar)
8. Zapp pretending to be a gentleman
9. Zapp blowing up DOOP headquarters
10. Zapp on trial (start hurry-up, if player fails to make the shot before the timer runs out, everytime the player shoots the orbit in Main Mode it will start the hurry up until they finally make it
11. Cartoon Zapp Brannigan adventures
12. Invisible spacecraft built for 1 (series of hurry-ups)

**Fry, Bender and Leila targets-**

Advance the plot lines for each of the 3 main characters by hitting their targets:

Fry

Bender

Leila

**Crew Drop Targets:**

There are drop targets for the main crew of Planet Express: Nibbler, Hermes, Zoidberg, Amy and the Professor. When any drop target is hit it starts a timer before the bank is reset and any lowered targets are popped back up to their raised position. Hitting a target in the base mode scores 1 point x the Character Multiplier of the target, as well as adds 1 Character XP.

**Crew Experience and Levels-**

The 8 crew members can each be “leveled up” by earning character XP. Character XP is earned by hitting a characters target on the playfield or by completing modes or combos that award XP.

Every level advancement increases that character’s multiplier, which are used in the modes and minimally in the main game mode to effect scoring. Additionally, every crew member that reaches level 2 increases the Crew Multiplier by 1, which directly effects the spinner scoring. Spinner value starts at 1 point per 120 degree turn, but increases up to 9 points per 120 degree turn with the crew multiplier maxed out.

**Dark Matter (right ramp)-**

Shoot the right ramp to hit the spinner and increase the amount of dark matter in the Planet Express’ fuel tank. Building up enough dark matter lights the shot to start a delivery, and having a full or half-full tank also provides specific benefits in certain modes.

**Deliveries-**

Filling the fuel tank with dark matter lights the scoop shot to start a delivery. There are 4 tiers of deliveries, for the first 3 tiers the player needs to only complete 1 delivery (out of multiple random options) to move on to the next tier. Failing to complete a delivery (ball drain or time-out) results in the player having to try another (or the same) delivery before they can progress to the next tier. For tiers 1-3, the amount of dark matter required to start the delivery increases at each tier until the player reaches tier 4, where deliveries always require a full tank of dark matter and each delivery is only available for one attempt.

**Tier 1 – ¼ tank of dark matter**

\-The moon (+fry, +leela)

\-Vergon 6 (+nibbler, + leela)

\-Robot Homeworld 1 (+bender)

**Tier 2 – ½ tank of dark matter**

\-“My 3 Suns” planet (+fry)

\-Big ball of garbage (+professor)

\-Robot Hell 1 (+bender)

\-Juan Valdiz SuperTanker Haul

**Tier 3 – ¾ tank of dark matter**

\-Titanic (bender)

\-Sewers 1 (+bender, +nibbler, +leela)

\-Cyclopia “Leela’s Homeworld” (Leela)

**\-**Deep South/Lost City of Atlanta (zoidberg, fry)

**Tier 4 – full tank of dark matter**

**Wizard Modes:**

**Forward Time Machine – (Professor)**

**Benderama – (Bender)**

**Mobius Dick – (Leila)**

**Central Bureaucracy “Born to be a Bureaucrat” – (Hermes)**

**Save the Universe from Giant Brains – (Nibbler)**

**Roswell That Ends Well – (Fry)**

**Wong Casino Vault Heist – (Zoidberg)**

**Evil Alien Cat Earth Energy Ray – (Amy)**

**Game Features:**

4a – Boards

Power Entry Board

PC

P3ROC MPU

SW-16 Switch Nodes

Opto Break-out board

PD-16 Driver Node

PD-LED light controller

Servo controller

4b – Power Circuit

The machine connects to a 120v wall outlet with a standard power cable (15a rated or above) which connects in the bottom right corner of the back box. This is also where the main on/off switch for the machine is located. There is a 10amp fuse in the power connector box that can be accessed by removing a small cover next to the power switch.

Inside the back box, the 110v is split, with the first set of wires going to the power entry board, and the second one to the PC and monitor. We should install a 3 fuse holding bracket with the power to the power entry board going through a 7a fuse, power to the PC through a 4a fuse, and power to the monitor through a 1 amp fuse. The power entry board connects to 2 solid state power supplies; the first provides 48vdc for the coils, the second provides 5vdc and 12vdc to power the node boards, lights, and switches.

**Diagram of power circuit including power connector box, power entry board, pc, and solid state power supplies.**

The 5vdc and 12vdc are sent back to the power entry board, which in turn closes a relay that enables the 48vdc. _At some future point we may install a computer controlled relay that can enable or disable the 48vdc however for now the relay is wired to be closed as long as there is 5vdc and 12vdc on the power entry board._

The MPU and all the node boards get power through the power entry board, as follows:

**PD-16:**

5vdc – Logic Power - J1

48vdc – Bank A – J5

48vdc – Bank B – J6

**PD-LED:**

5vdc – Power – J1

**SW-16:** (note there are 3 of these, numbered 0, 1 and 2)

12vdc – Power – J1

**P3ROC MPU:**

5vdc – Power – J2

**\*note that the Opto breakout board is powered off the 12vdc from SW-16-1**

**Come back and add notes about power to the servo controller once it has been added.**

4c – Switches and Optos

Switch Chart:

| **Switch** | **Type** | **Board/Bank** | **Position** | **MPF#** |
| --- | --- | --- | --- | --- |
| s_trough_jam | opto | 1J6 | 7   | A0-B1-7 |
| s_trough1 | opto | 1J6 | 6   | A0-B1-6 |
| s_dt_hermes | opto DT | 1J6 | 5   | A0-B1-5 |
| s_dt_amy | opto DT | 1J6 | 4   | A0-B1-4 |
| s_dt_professor | opto DT | 1J6 | 3   | A0-B1-3 |
| s_dt_zoidberg | opto DT | 1J6 | 2   | A0-B1-2 |
| s_dt_nibbler | opto DT | 1J6 | 1   | A0-B1-1 |
| s_suicidebooth | rollover | 1J6 | 0   | A0-B1-0 |
| s_left_outlane | rollover | 1J2 | 7   | A0-B0-7 |
| s_left_inlane | rollover | 1J2 | 6   | A0-B0-6 |
| s_left_sling | leaf | 1J2 | 5   | A0-B0-5 |
| s_right_sling | leaf | 1J2 | 4   | A0-B0-4 |
| s_cap1 | star | 1J2 | 3   | A0-B0-3 |
| s_r_outlane | rollover | 1J2 | 2   | A0-B0-2 |
| s_trough2 | micro roller | 1J2 | 1   | A0-B0-1 |
| s_trough3 | micro roller | 1J2 | 0   | A0-B0-0 |
| s_PE_platter | opto | 2J6 | 7   | A1-B1-7 |
| s_left_ramp | opto | 2J6 | 6   | A1-B1-6 |
| s_left_loop | opto | 2J6 | 5   | A1-B1-5 |
| s_VUK | opto | 2J6 | 4   | A1-B1-4 |
| s_right_loop | opto | 2J6 | 3   | A1-B1-3 |
| s_r_orbit | opto | 2J6 | 2   | A1-B1-2 |
| s_right_return | micro | 2J6 | 1   | A1-B1-1 |
| s_shooter_lane | rollover | 2J6 | 0   | A1-B1-0 |
| s_cap2 | star | 2J2 | 7   | A1-B0-7 |
| s_cap3 | star | 2J2 | 6   | A1-B0-6 |
| s_cap4 | star | 2J2 | 5   | A1-B0-5 |
| s_pop_bumper | leaf | 2J2 | 4   | A1-B0-4 |
| s_t_leela | target | 2J2 | 3   | A1-B0-3 |
| s_t_fry | target | 2J2 | 2   | A1-B0-2 |
| s_t-bender | target | 2J2 | 1   | A1-B0-1 |
| s_right_ramp | micro | 2J2 | 0   | A1-B0-0 |
| s_left_flipper | OptoPCB | 3J2 | 5   | A2-B0-5 |
| s_hypnotoad_button | leaf | 3J2 | 3   | A2-B0-3 |
| s_start | micro assembly | 3J2 | 6   | A2-B0-6 |
| s_hedonismbot | target | 3J2 | 2   | A2-B0-2 |
| s_right_flipper | OptoPCB | 3J2 | 0   | A2-B0-0 |

4d – Coils

| **coil** | **type** | **board/bank** | **mpf#** |
| --- | --- | --- | --- |
| c_dt_hermes_down |     | 1A  | a1-b0-0 |
| c_dt_amy_down |     | 1A  | a1-b0-1 |
| c_dt_professor_down |     | 1A  | a1-b0-2 |
| c_dt_zoidberg_down |     | 1A  | a1-b0-3 |
| c_dt_nibbler_down |     | 1A  | a1-b0-4 |
| empty |     | 1A  | a1-b0-5 |
| c_left_flipper_main |     | 1A  | a1-b0-6 |
| c_left_flipper_hold |     | 1A  | a1-b0-7 |
| c_dt_hermes_up |     | 1B  | a1-b1-0 |
| c_dt_amy_up |     | 1B  | a1-b1-1 |
| c_dt_professor up |     | 1B  | a1-b1-2 |
| c_dt_zoidberg_up |     | 1B  | a1-b1-3 |
| c_dt_nibbler_up |     | 1B  | a1-b1-4 |
| empty |     | 1B  | a1-b1-5 |
| c_right_flipper_main |     | 1B  | a1-b1-6 |
| c_right_flipper_hold |     | 1B  | a1-b1-7 |
| c_plunger |     | 3A  | a3-b0-7 |
| c_trough_eject |     | 3A  | a3-b0-6 |
| c_kickback |     | 3A  | a3-b0-5 |
| c_sling_right |     | 3A  | a3-b0-4 |
| c_sling_left |     | 3A  | a3-b0-3 |
| c_pop_bumper |     | 3A  | a3-b0-2 |
| Gate |     | 3A  | a3-b0-1 |
| empty |     | 3A  | a3-b0-0 |
| empty |     | 3B  | a3-b1-0 |
| c_magnet |     | 3B  | a3-b1-1 |
| c_VUK |     | 3B  | a3-b1-2 |
| c_post_right |     | 3B  | a3-b1-3 |
| c_post_left |     | 3B  | a3-b1-4 |
| empty |     | 3B  | a3-b1-5 |
| empty |     | 3B  | a3-b1-6 |
| empty |     | 3B  | a3-b1-7 |

4e – Lights

PD-LED board headers-

(add image later)

Lamp Chart:

| Name | Number | Connector/pin | Type: |
| --- | --- | --- | --- |
|     | 0, 1, 2 | J5/2-4 | RGB General |
|     | 3, 4, 5 | J5/7-9 | RGB General |
|     | 6, 7, 8 | J5/12-14 | RGB General |
|     | 9, 10, 11 | J5/17-19 | RGB Feature |
|     | 12, 13, 14 | J9/2-4 |     |
|     | 15, 16, 17 | J9/7-9 |     |
|     | 18, 19, 20 | J9/12-14 |     |
|     | 21, 22, 23 | J9/17-19 |     |
|     | 24, 25, 26 | J6/2-4 | RGB General |
|     | 27, 28, 29 | J6/7-9 | RGB General |
|     | 30, 31, 32 | J6/12-14 | RGB Feature |
| pe_platter_2 | 33, 34, 35 | J6/17-19 | RGB Feature |
| cap3 | 36, 37, 38 | J10/2-4 | Insert |
| pop_bumper | 39, 40, 41 | J10/7-9 | RGB Feature |
| r_loop | 42, 43, 44 | J10/12-14 | RGB Feature |
| r_orbit | 45, 46, 47 | J10/17-19 | RGB Feature |
| 2x_scoring | 48, 49, 50 | J7/2-4 | Insert |
| 3x_scoring | 51, 52, 53 | J7/7-9 | Insert |
| cap1 | 54, 55, 56 | J7/12-14 | Insert |
| cap2 | 57, 58, 59 | J7/17-19 | Insert |
| r_laneguide | 60, 61, 62 | J11/2-4 | RGB General |
| r_outlane | 63, 64, 65 | J11/7-9 | Insert |
| cap4 | 66, 67, 68 | J11/12-14 | Insert |
| r-slingshot | 69, 70, 71 | J11/17-19 | RGB General |
| l_laneguide | 72, 73, 74 | J8/2-4 | RGB General |
| l_inlane | 75, 76, 77 | J8/7-9 | Insert |
| l_slingshot | 78, 79, 80 | J8/12-14 | RGB General |
| shoot_again | 81, 82, 83 | J8/17-19 | Insert |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
|     |     |     |     |
