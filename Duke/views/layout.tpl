<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Duke</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/styles.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/menu.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
        <div class="top_panel_wrapper" id="topPanel">
        <div class="navbar_wrapper">
            <nav>
                <div class="center dropdown">
                    <a href="./about">О НАС</a>
                    <a href="./main">ГЛАВНАЯ</a>
                    <div class="tasks">
                        <a href="#" id="tasksText">ЗАДАЧИ</a>                    
                        <ul class="ul-dropdown">
                            <li class="li-dropdown"><a class="a-dropdown" href="./firstVar">ВАРИАНТ 1</a>
                            <li class="li-dropdown"><a class="a-dropdown" href="./secondVar">ВАРИАНТ 2</a>  
                            <li class="li-dropdown"><a class="a-dropdown" href="./thirdVar">ВАРИАНТ 3</a>  
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
            <p class="rightAlignment" class="wrapper">dukecorp@internet.re</p>
        </footer>
    </div>

    <div id="modalCard" class="modal-card modal-pop-up">
        <div>
           <h2>Переход на другую страницу</h2>
           <hr>
           <p class="link-text" id="modalText">Вы уверены, что хотите перейти на страницу: </p>
           <div class="modal-pop-up-content">
                <button id="modalYes"> 
                    Да
                </button>
                <button id="modalNo">
                    Нет
                </button>
                </div>
            </div>
        </div>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>
    <script src="/static/scripts/site-scripts.js"></script>
</body>
</html>