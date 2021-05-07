<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<br />
<p align="center">

  <h3 align="center">proxyCalendar</h3>

  <p align="center">
    A Python web server script to manipulate a City of Calgary Solid waste cart calendar.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### The Problem
While I like that the City Of Calgary has a calendar of the solid waste collection schedule (cuz it changes!), 
it has it's problems when used with Google Calendar:
![image](https://user-images.githubusercontent.com/1638313/117516488-7a5e9800-af56-11eb-9d48-335fb2410fdc.png)


1. The Blue and Green cart pickup events are combined when they are picked up on the same day.   This is a problem since Google Calendar only shows the first 10 to 15 characters of the event summary (so at a glance it shows "Blue cart ..." even if the event is for Blue and Green carts).
2. All three carts are delivered with one calendar and Google allows only one color per calendar.

### The Solution

You need a web server under your control, that can run Python CGI scripts.  The ical.py script contains the URL used to get the calendar for your neighbourhood (so you need to replace that), then filters the events per cart color.

You then add three calendars to your Google Calendar:

1.  http://..../ical.py?cart=Blue
2.  http://..../ical.py?cart=green
3.  http://..../ical.py?cart=Black

(note the case of the parameters) and color them appropriately.

![image](https://user-images.githubusercontent.com/1638313/117516446-5733e880-af56-11eb-8837-fdc7c51ad45a.png)

Much better!


### Built With

Python 3

## Getting Started
### Installation

## Usage

<!-- ROADMAP -->
## Roadmap


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

Brent Fraser - - info@geoanalytic.com  


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements


