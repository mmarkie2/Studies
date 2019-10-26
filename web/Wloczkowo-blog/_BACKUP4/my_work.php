<?php session_start();require_once 'error_report.php';?>

<!DOCTYPE html>
<html lang="pl">

<head>
	<meta charset="utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
	
	<title>Włóczkowo</title>
	<meta name="description" content="Moje włóczki" />
    <meta name="keywords" content="blog, włóczki, sznurek" />
    <meta name="author" content="Kamil Cinner">
    
    <link href="https://fonts.googleapis.com/css?family=Akronim&display=swap&subset=latin-ext" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Farsan&display=swap&subset=latin-ext" rel="stylesheet">

    <link href="main.css" rel="stylesheet" type="text/css"/>
    <link rel="stylesheet" href="css/fontello.css">

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="jquery.scrollTo.min.js"></script>
    <script src="scroll.js"></script>
    <script src="load_fibers_data.js"></script>
</head>

<body>
    <header>
        <div class="logo"><a href="index.php">Włóczkowo</a></div>

        <a href="#" class="scrollup"></a>

        <nav id="topnav">
            <ul class="menu">
                <li><a href="#">Aktualności</a></li>
                <li><a href="#">Moje włóczki</a></li>
                <li><a href="#">Moje prace</a></li>
                <li><a href="#">Kontakt</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <article>
            <section id="newest"></section>
        </article>
    </main>

    <footer>
        <div class="socials">
			<div class="socialdivs">
                <a href="#">
                    <div class="fb">
					    <i class="icon-facebook-official"></i>
				    </div>
                </a>
				
                <a target="_blank" href="https://www.instagram.com/wloczkowo/">
                    <div class="ig">
                        <i class="icon-instagram"></i>
                    </div>
                </a>
                
				<div style="clear:both"></div>
			</div>
        </div>
        
		<div class="info">
            Wszelkie prawa zastrzeżone &copy; 2019 Dziękuję za wizytę!
            <br/>
            Wykonał Kamil Cinner
		</div>
    </footer>
</body>

</html>