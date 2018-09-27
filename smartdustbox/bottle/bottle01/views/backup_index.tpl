<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>

        <!-- load css files -->
        <link rel="stylesheet" href="static/css/bootstrap.min.css">
    </head>
    <body>
        <main>
        <!-- <a href="#" class="btn" id="checkbox-led-0" >BUTTON</a><br> -->


        <p class="shadow">Controlleraaaa</p>
            <div>
                <br>
                <h2>test_checkbox</h2>
                  <div class="foo">
                    <span class="letter" data-letter="A">A</span>
                    <span class="letter" data-letter="B">B</span>
                    <span class="letter" data-letter="C">C</span>
                    <span class="letter" data-letter="D">D</span>
                    <span class="letter" data-letter="E">E</span>
                    <span class="letter" data-letter="F">F</span>
                    <span class="letter" data-letter="G">G</span>
                    <span class="letter" data-letter="H">H</span>
                    <span class="letter" data-letter="I">I</span>
                    <span class="letter" data-letter="L">L</span>
                    <span class="letter" data-letter="M">M</span>
                    <span class="letter" data-letter="N">N</span>
                    <span class="letter" data-letter="O">O</span>
                    <span class="letter" data-letter="P">P</span>
                    <span class="letter" data-letter="Q">Q</span>
                    <span class="letter" data-letter="R">R</span>
                    <span class="letter" data-letter="S">S</span>
                    <span class="letter" data-letter="T">T</span>
                    <span class="letter" data-letter="U">U</span>
                    <span class="letter" data-letter="V">V</span>
                    <span class="letter" data-letter="Z">Z</span>
                  </div>
                    <div class="plate">
                      <p class="script"><span>Handwritey</span></p>
                      <p class="shadow text1">CHUNKY</p>
                      <p class="shadow text2">BIG</p>
                      <p class="shadow text3">STUFF</p>
                      <p class="script"><span>with CSS</span></p>
                    </div>

                    <label>
                      <input type="checkbox" name="checkbox01[]" class="checkbox01-input" onclick="setLed('0', this.checked)">
                      <span class="checkbox01-parts">LED00</span><br><br>
                    </label>
                <hr>
            </div>
            <div>
                <h2>LED</h2>
                LED0: <input type="checkbox" id="checkbox-led-0" name="checkbox-led-0" data-on-color="primary" onclick="setLed('0', this.checked)"><br>
                LED1: <input type="checkbox" id="checkbox-led-1" name="checkbox-led-1" data-on-color="primary" onclick="setLed('1', this.checked)"><br>
                <hr>
            </div>
            <div>
                <h2>Button</h2>
                Button0: <input type="checkbox" id="checkbox-button-0" name="checkbox-button-0" data-on-color="primary"><br>
                Button1: <input type="checkbox" id="checkbox-button-1" name="checkbox-button-1" data-on-color="primary">
                <hr>
            </div>
        </div>
        </main>
        <!-- load script files -->
        <script type="text/javascript" src="static/js/caller.js" charset="utf-8"></script>
    </body>
</html>
