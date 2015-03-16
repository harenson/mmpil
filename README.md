#Martyr2's Mega Project Ideas List [>](http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/)

**Categories:**
[Text](#text) ~ [Networking](#networking) ~ [Classes](#classes) ~ [Threading](#threading) ~ [Web](#web) ~ [Files](#files) ~ [Databases](#databases) ~ [Graphics and Multimedia](#graphics-and-multimedia) ~ [Games](#games)


##Text

######<del>[Reverse a String:](https://github.com/harenson/mmpil/blob/master/text/reverse_string.py)</del>
    Enter a string and the program will reverse it and print it out.

######PigLatin:
    Pig Latin is a game of alterations played on the English language game.
    To create the Pig Latin form of an English word the initial consonant sound
    is transposed to the end of the word and an ay is affixed (Ex.: "banana"
    would yield anana-bay). Read Wikipedia for more information on rules.

######<del>[CountVowels:](https://github.com/harenson/mmpil/blob/master/text/count_vowels.py)</del>
    Enter a string and the program counts the number of vowels in the text.
    For added complexity have it report a sum of each vowel found.

######<del>[Checkif Palindrome:](https://github.com/harenson/mmpil/blob/master/text/palindrome.py)</del>
    Checks if the string entered by the user is a palindrome.
    That is that it reads the same forwards as backwards like “racecar”

######<del>[CountWords in a String:](https://github.com/harenson/mmpil/blob/master/text/count_words.py)</del>
    Counts the number of individual words in a string. For added complexity
    read these strings in from a text file and generate a summary.

######TextEditor:
    Notepad style application that can open, edit, and save text documents.
    Add syntax highlighting and other features.

######RSSFeed Creator:
    A program which can read in text from other sources and put it in RSS
    or Atom news format for syndication.

######Postit Notes Program:
    A program where you can add text reminders and post them. You can have
    the program also add popup reminders.

######QuoteTracker (market symbols etc):
    A program which can go out and check the current value of stocks for a list
    of symbols entered by the user. The user can set how often the stocks are
    checked and the program can show green up and red down arrows to show
    which direction the stock value has moved.

######Guestbook/ Journal:
    A simple application that allows people to add comments or write journal
    entries. It can allow comments or not and timestamps for all entries.
    Could also be made into a shout box.

######NewsTicker and Game Scores:
    A program which sits on your desktop and aggregates news and game scores
    from various sources on the net. It then scrolls them across the screen
    on regular intervals.

######FortuneTeller (Horoscope):
    A program that checks your horoscope on various astrology sites and puts
    them together for you each day.

######Vigenere/ Vernam / Ceasar Ciphers:
    Functions for encrypting and decrypting data messages. Then send them to
    a friend.

######RandomGift Suggestions:
    Enter various gifts for certain people when you think of them. When its
    time to give them a gift (xmas, birthday, anniversary) it will randomly
    pick one and perhaps places you can get it.

######Text to HTML Generator:
    Converts text files into web HTML files and stylizes them. Great for making
    online documentation of standard text documentation.

######CDKey Generator:
    Generates a unique key for your applications to use based on some arbitrary
    algorithm that you can specify. Great for software developers looking to
    make shareware that can be activated.

######RegexQuery Tool:
    A tool that allows the user to enter a text string and then in a separate
    control enter a regex pattern. It will run the regular expression against
    the source text and return any matches or flag errors in the regular
    expression.



##Networking [^][top]

######FTPProgram:
    A file transfer program which can transfer files back and forth from a
    remote web sever.

######GetAtomic Time from Internet Clock:
    This program will get the true atomic time from an atomic time clock on the
    Internet. There are various clocks across the world. Do a search for a list
    of them.

######ChatApplication (IRC or MSN Style):
    Create a chat application that can create simple chat rooms like on
    Internet Relay Chat (IRC) or a more direct chatting style like MSN. For
    added complexity, create your own protocol to facilitate this chatting.

######FetchCurrent Weather:
    Get the current weather for a given zip/postal code. 

######P2PFile Sharing App:
    Create a program like LimeWire, FrostWire, Bearshare, or a torrent style
    application.

######PortScanner:
    Enter an IP address and a port range where the program will then attempt
    to find open ports on the given computer by connecting to each of them.
    On any successful connections mark the port as open.

######MailChecker (POP3 / IMAP):
    The user enters various account information include web server and IP,
    protocol type (POP3 or IMAP) and the application will check for email on
    several accounts at a given interval.

######PacketSniffer:
    A utility program that will read packets coming in and out of the machine
    along with related information like destination and payload size.

######Countryfrom IP Lookup:
    Enter an IP address and find the country that IP is registered in.

######WhoisSearch Tool:
    Enter an IP or host address and have it look it up through whois and return
    the results to you.

######Zip/ Postal Code Lookup:
    Enter a zip or postal code and have it return which city/cities that are in
    that zip code.

######RemoteLogin:
    Create a remote desktop style application which can see and control the
    remote computer (given you have permissions). It may require the use of
    your own private network and a second computer to test with.

######SiteChecker with Time Scheduling:
    An application that attempts to connect to a website or server every so
    many minutes or a given time and check if it is up. If it is down, it will
    notify you by email or by posting a notice on screen.

######SmallWeb Server:
    A simple web server that can serve HTML files that contain Javascript and
    other forms of non-code executing code. Added complexity would be to try
    and implement streaming video, create a server-side language, or serve up
    other stream types.

######WebBot:
    An automated program which carries out tasks on the web including checking
    websites, page scraping, and summarization of data or web posting.



##Classes [^][top]

######<del>[ProductInventory Project:](https://github.com/harenson/mmpil/blob/master/classes/product_inventory/)</del>
    Create an application which manages an inventory of products. Create a
    product class which has a price, id, and quantity on hand. Then create an
    inventory class which keeps track of various products and can sum up the
    inventory value.

######<del>[MovieStore:](https://github.com/harenson/mmpil/blob/master/classes/movie_store/)</del>
    Manage video rentals and controls when videos are checked out, due to
    return, overdue fees and for added complexity create a summary of those
    accounts which are overdue for contact.

######Airline/ Hotel Reservation System:
    Create a reservation system which books airline seats or hotel rooms. It
    charges various rates for particular sections of the plane or hotel.
    Example, first class is going to cost more than coach. Hotel rooms have
    penthouse suites which cost more. Keep track of when rooms will be
    available and can be scheduled.

######StudentGrade Book Application:
    Keep track of students (with a student class that has their name, average,
    and scores) in a class and their grades. Assign their scores on tests and
    assignments to the students and figure out their average and grade for the
    class. For added complexity put the students on a bell curve.

######BankAccount Manager:
    Create a class called “Account” which will be an abstract class for three
    other classes called “CheckingAccount”, “SavingsAccount” and
    “BusinessAccount”. Manage credits and debits from these accounts through
    an ATM style program.

######LibraryCatalog:
    Create a book class with a title, page count, ISBN and whether or not it is
    checked out or not. Manage a collection of various books and allow the user
    to check out books or return books. For added complexity generate a report
    of those books overdue and any fees. Also allow users to put books on
    reserve.



##Threading [^][top]

######CreateA Progress Bar for Downloads:
    Create a progress bar for applications that can keep track of a download in
    progress. The progress bar will be on a separate thread and will
    communicate with the main thread using delegates.

######DownloadManager:
    Allow your program to download various files and each one is downloading in
    the background on a separate thread. The main thread will keep track of the
    other thread’s progress and notify the user when downloads are completed.

######ChatApplication (remoting style):
    Create a chat application which allows you to connect directly to another
    computer by their IP through the use of remoting and allow your “server”
    application handle multiple incoming connections.

######BulkThumbnail Creator:
    Picture processing can take a bit of time for some transformations.
    Especially if the image is large. Create an image program which can take
    hundreds of images and converts them to a specified size in the background
    thread while you do other things. For added complexity, have one thread
    handling re-sizing, have another bulk renaming of thumbnails etc.



##Web [^][top]

######WYSIWG(What you see is what you get) Editor:
    Create an editor online which allows people to move around elements, create
    tables, write text, set colors etc for web pages without having to know
    HTML. Think Dreamweaver or FrontPage but for online sites. If you need an
    example check out the DIC page used to create a post.

######WebBrowser with Tabs:
    Create a small web browser that allows you to navigate the web and contains
    tabs which can be used to navigate to multiple web pages at once. For
    simplicity don’t worry about executing Javascript or other client side code.

######PageScraper:
    Create an application which connects to a site and pulls out all links, or
    images, and saves them to a list. For added complexity, organize the
    indexed content and don’t allow duplicates. Have it put the results into
    an easily searchable index file.

######FileDownloader:
    An application which can download various objects on a page including video
    streams or all files on a page. Great for pages with a lot of download
    links.

######TelnetApplication:
    Create an application which can telnet into servers across the internet and
    run basic commands. 

######OnlineWhite Board:
    Create an application which allows you and friends to collaborate on a
    white board online. Draw pictures, write notes and use various colors to
    flesh out ideas for projects. For added complexity try building in picture
    tubes.

######BandwidthMonitor:
    A small utility program that tracks how much data you have uploaded and
    downloaded from the net during the course of your current online session.
    See if you can find out what periods of the day you use more and less and
    generate a report or graph that shows it.

######BookmarkCollector and Sorter:
    An application that you can put online for people to upload bookmarks to,
    have it sort them, remove duplicates and export the entire list as a
    Firefox/IE/Safari bookmark file. For added complexity see if you can group
    the bookmark items into various folders.

######PasswordSafe:
    A program which keeps track of passwords for sites or applications and
    encrypts them with a key so that no one can read them.

######MediaPlayer Widget for iGoogle:
    Create an iGoogle gadget which can play various song lists from your
    computer as well as share one song daily. Perhaps let people look up which
    songs you have listened to lately.

######TextBased Game Like Utopia:
    Create a simple text based RPG like Utopia where you can create a
    civilization, gather resources, forge alliances, cast spells and more on a
    turn based system. See if you can dominate the kingdom.

######ScheduledAuto Login and Action:
    Make an application which logs into a given site on a schedule and invokes
    a certain action and then logs out. This can be useful for checking web
    mail, posting regular content, or getting info for other applications and
    saving it to your computer.

######E-CardGenerator:
    Make a site that allows people to generate their own little e-cards and
    send them to other people. Can use flash or not. Use a picture library and
    perhaps insightful mottos or quotes.

######ContentManagement System:
    Create a content management system (CMS) like Joomla, Drupal, PHP Nuke etc.
    Start small and allow for the addition of modules/addons later.

######TemplateMaker:
    Make a site or application which allows the user to enter in various color
    codes, elements, dimensions and constructs a template file for a particular
    application like PHPBB, Invision Board, MySpace, Bebo, etc.

######CAPTCHAMaker:
    Ever see those images with letters a numbers when you signup for a service
    and then asks you to enter what you see? It keeps web bots from
    automatically signing up and spamming. Try creating one yourself for online
    forms. If you use PHP, take a look at the image functions of GD.



##Files [^][top]

######QuizMaker:
    Make an application which takes various questions form a file, picked
    randomly, and puts together a quiz for students. Each quiz can be different
    and then reads a key to grade the quizzes.

######QuickLauncher:
    A utility program that allows the user to assign various programs to icons
    on a toolbar. Then by clicking the buttons they can quickly launch the
    programs with parameters etc. Much like Windows quick launch.

######FileExplorer:
    Create your own windows explorer program but with added features, better
    searching, new icons and other views.

######SortFile Records Utility:
    Reads a file of records, sorts them, and then writes them back to the file.
    Allow the user to choose various sort style and sorting based on a
    particular field.

######AddTransactions In File and Find Averages:
    Read in a file of financial transactions, group them into accounts, add up
    fields or find averages or apply credits and debits to each account.

######CreateZip File Maker:
    The user enters various files from different directories and maybe even
    another computer on the network and the program transfers them and zips
    them up into a zip file. For added complexity, apply actual compression to
    the files.

######PDFGenerator:
    An application which can read in a text file, html file or some other file
    and generates a PDF file out of it. Great for a web based service where the
    user uploads the file and the program returns a PDF of the file.

######BulkRenamer and Organizer:
    This program will take a series of files and renames them with a specific
    filename filter entered by the user. For instance if the user enters
    myimage###.jpg it will rename all files with a “minimum” of three numbers
    like “myimage001.jpg”, “myimage145.jpg” or even “myimage1987.jpg” since
    1987 has at least three numbers.

######Mp3Tagger:
    Modify and add ID3v1 tags to MP3 files. See if you can also add in the
    album art into the MP3 file’s header as well as other ID3v2 tags.

######LogFile Maker:
    Make an application which logs various statistics in response to given
    events. This can be something that logs what an application does, what
    the system is doing, when something like a file changes etc.

######ExcelSpreadsheet Exporter:
    Create an online application which can read in a file and create an Excel
    Spreadsheet to export back. This can be through CVS or other file formats.
    For added complexity, see if you can create formula fields as well.

######RPGCharacter Stat Creator:
    Make a program which will randomly create a character’s stats based on
    several rules set forth by the user. Have it generate a class, gender,
    strength/magic/dexterity points, and extra abilities or trades. Have it
    save it to a file which can then be printed out by a dungeon master.

######ImageMap Generator:
    Image maps are those images on the web that have multiple hover points that
    link to different pages. Such images may include maps or splash pages. See
    if you can make one where the user specifies an image, clicks hotspots in
    the image and specify links. It will then generate the HTML code to a file
    that the user can then copy and paste into their website to make the image
    map.

######FileCopy Utility:
    Create a utility that can do bulk file copying and backups of other files.

######CodeSnippet Manager:
    Another utility program that allows coders to put in functions, classes or
    other tidbits to save for use later. Organized by the type of snippet or
    language the coder can quickly look up code. For extra practice try adding
    syntax highlighting based on the language.

######VersioningManager:
    Create your own versioning system for code files. Users are forced to check
    out items and lock items during reading and writing so that a group of
    programmers are not accidentally overwriting code files on one another.



##Databases [^][top]

######SQLQuery Analyzer:
    A utility application which a user can enter a query and have it run
    against a local database and look for ways to make it more efficient.

######RemoteSQL Tool:
    A utility that can execute queries on remote servers from your local
    computer across the Internet. It should take in a remote host, user name
    and password, run the query and return the results.

######Baseball/ Other Card Collector:
    Create an online application for keeping track of a collection of cards.
    Let the user enter all cards in a set, check off which ones they have,
    which ones they need and generate lists of cards they are looking for. For
    extra complexity, have it sum up sets and generate reports on how close
    they are of completing sets or the current value of a set.

######ReportGenerator:
    Create a utility that generates a report based on some tables in a
    database. Generates a sales reports based on the order/order details tables
    or sums up the days current database activity.

######DatabaseBackup Script Maker:
    A program which reads a database’s objects, relationships, records and
    stored procedures and creates a .sql file which can then be imported into
    another database or kept as a backup file to rebuild the database with.

######EventScheduler and Calendar:
    Make an application which allows the user to enter a date and time of an
    event, event notes and then schedule those events on a calendar. The user
    can then browse the calendar or search the calendar for specific events.
    For added complexity, allow the application to create reoccurrence events
    that reoccur every day, week, month, year etc.

######BudgetTracker:
    Write an application that keeps track of a household’s budget. The user can
    add expenses, income, and recurring costs to find out how much they are
    saving or losing over a period of time. For added complexity allow the user
    to specify a date range and see the net flow of money in and out of the
    house budget for that time period.

######AddressBook:
    Keep track of various contacts, their numbers, emails and little notes
    about them like a Rolodex in the database. For extra complexity, allow the
    user to connect to a website publish their address book based on specific
    options the user has set.

######TVShow Tracker:
    Got a favorite show you don’t want to miss? Don’t have a PVR or want to be
    able to find the show to then PVR it later? Make an application which can
    search various online TV Guide sites, locate the shows/times/channels and
    add them to a database application. The database/website then can send you
    email reminders that a show is about to start and which channel it will be
    on.

######TravelPlanner System:
    Make a system that allows users to put together their own little travel
    itinerary and keep track of the airline / hotel arrangements, points of
    interest, budget and schedule. 

######EntityRelationship Diagram (ERD) Creator:
    A program that allows the user to put together ERD diagram and save it or
    have it generate some basic SQL syntax to give them a jump start.

######DatabaseTranslation (MySQL <- SQL Server):
    A simple utility that reads in from one database and constructs SQL
    compliant with another database. Then saves that to another database. One
    popular transition would be to and from MySQL server for databases like SQL
    Server and Oracle.

######WebBoard (Forum):
    Create a forum for you and your buddies to post, administer and share
    thoughts and ideas.



##Graphics and Multimedia [^][top]

######SlideShow:
    Make an application that shows various pictures in a slide show format. For
    extra complexity try adding various effects like fade in/out, star wipe and
    window blinds transitions.

######MindMapper:
    Allow the user to put down ideas and quickly brainstorm how they are
    related into a mind map. The goal here is speed so let the user quickly
    write in an idea and drag it around in a visual map to show relationships.

######ImportPicture and Save as Grayscale:
    A utility that sucks the color right out of an image and saves it. You
    could add more including adjusting contrast, colorizing and more for added
    complexity.

######StreamVideo from Online:
    Try to create your own online streaming video player.

######Mp3Player (and Other Formats):
    A simple program for playing your favorite music files. For extra
    complexity see if you can add in playlists and an equalizer.

######BulkPicture Manipulator:
    This program will take in a directory of pictures and apply a certain
    effect to them whether it be reducing color count, changing its format, or
    alter file attributes. For something extra try to see if you can also
    create a system to tag them. 

######CDBurning App:
    Create a utility that simply burns data to a CD.

######YouTubeDownloader:
    A program which can download videos to your hard drive from youtube.com.
    Save the files in various formats including FLV and AVI.

######WallpaperManager:
    Make a program which keeps track of your favorite wallpapers, changes them
    regularly and maybe even re-sizes them for your resolution (aka tiles one
    and stretches another)

######ScreenCapture Program:
    Make a utility that will simply capture a frame from your web cam. For
    added complexity see if you can also build in emailing functionality.

######ImageBrowser:
    This application is used to view various image files on your computer from
    PNG, GIF, JPG to BMP, TIFF etc.

######TrafficLight Application:
    See if you can make your own street light application and then put it into
    an intersection scenario. Don’t let any cars run the lights and crash into
    one another!

######MP3to Wav Converter:
    MP3 is essentially compressed wav format. See if you can translate it back
    into wav so that some other sound editing programs can work with the wav
    file itself. Keep in mind that 1 MB of MP3 is relative 10MB wav.

######SignatureMaker:
    Ever seen those web board posts where someone has a generated signature
    made up? See if you can make a program that allows the user to specify a
    background, text, colors and alignment to make their own signatures or
    userbars.

######ScreenSaver:
    Make a screensaver program that will run while your computer sits idle.
    To make a simple one use some standard pictures and then for added
    complexity try a 3D object that spins around the screen and bounces off the
    sides.

######WatermarkingApplication:
    Have some pictures you want copyright protected? Add your own logo or text
    lightly across the background so that no one can simply steal your graphics
    off your site. Make a program that will add this watermark to the picture.

######TurtleGraphics:
    This is a common project where you create a floor of 20 x 20 squares. Using
    various commands you tell a turtle to draw a line on the floor. You have
    move forward, left or right, lift or drop pen etc. For added complexity,
    allow the program to read in the list of commands from a file. Do a search
    online for “Turtle Graphics” for more information.



##Games [^][top]

######Battleship:
    Create two game boards and let each player place a number of war ships.
    Each player can’t see the other person’s board. They then take turns firing
    at one another by guessing one of the board squares. If the square they
    guess contains part of a ship, it is a hit. Otherwise it is a miss. They
    sink a ship when all squares containing that particular ship have been
    uncovered. The player wins when all their opponents’ ships have been sunk.

######Chessand Checkers:
    Simply put a game of chess or checkers. Try to make it playable online and
    if you can use a graphical user interface that can also undo or redo a step
    as well as keep a history of moves for replay.

######Hangman:
    Randomly select a word from a file, have the user guess characters in the
    word. For each character they guess that is not in the word, have it draw
    another part of a man hanging in a noose. If the picture is completed
    before they guess all the characters, they lose.

######CrosswordPuzzle:
    Create a crossword puzzle which links words together on common letters.
    Provide a list of clues for each word and let the user enter fill in the
    words until the entire crossword is filled in.

######Frogger:
    Get your frog across the river and lanes of traffic by either jumping on
    logs and lily pads rushing by at different speeds or avoid the automobiles
    which are also moving at various speeds. Based on the old arcade game.

[top]:#martyr2s-mega-project-ideas-list- "top"
