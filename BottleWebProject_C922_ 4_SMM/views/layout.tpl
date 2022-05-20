<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duke</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/styles.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/menu.css" />
    <script src="/static/scripts/table-resize-handler.js"></script>
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <script src="/static/scripts/business-logic-integration.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

</head>

<body>
        <div class="top_panel_wrapper" id="topPanel">
        <div class="navbar_wrapper">
            <nav>
                <div class="center dropdown">
                    <a href="./about">О НАС</a>
                    <a href="./main">ГЛАВНАЯ</a>
                    <div class="tasks">
                        <a href="#" id="tasksText">ЗАДАНИЯ</a>          
                        <ul class="ul-dropdown">
                            <li class="li-dropdown"><a class="a-dropdown" href="./binary_relation_1">СВОЙСТВА ОТНОШЕНИЙ 1</a>
                            <li class="li-dropdown"><a class="a-dropdown" href="./binary_relation_2">СВОЙСТВА ОТНОШЕНИЙ 2</a>  
                            <li class="li-dropdown"><a class="a-dropdown" href="./max_flow">МАКСИМАЛЬНЫЙ ПОТОК</a>  
                        </ul>
                    </div>                      
                </div>
            </nav>
        </div>

        <div class="top-panel_overlay">
            <p class="letters-spacing">DUKE</p>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr/>
        <footer>
            <p class="wrapper">&copy; {{ year }} - Duke</p>
            <p class="rightAlignment wrapper">dukecorp@internet.re</p>
        </footer>
    </div>


    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
    <script src="/static/scripts/site-scripts.js"></script>
</body>
</html>