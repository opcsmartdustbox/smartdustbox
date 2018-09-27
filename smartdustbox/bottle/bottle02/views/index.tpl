<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Controller</title>

        <!-- load css files -->
        <link rel="stylesheet" href="static/css/bootstrap.min2.css">
    </head>
    <body>
    <center>
        <main>
          <br>
            <h2>Compass</h2>
            <div id="txt">ここにデータを表示</div>

            <br>
            <br>

            <h2>Slider</h2>
            <div>
              <!-- <input type="range" value="1" min="1" max="100" step="1" oninput="setLed('0', value=this.value)"> -->
              <form oninput="k.value = a.value">
                <output name="k" ></output><br>
                <input type="range" min="1" max="100" step="1" id="a" value="50" oninput="setLed('0', this.value); aaa(this.value)"><br>
                <br>
              </form>

              <!-- <input type="range" class="input-range" value="100" min="0" max="200" data-unit="%"> -->
            </div>
            <div>
              <h1>Chart</h1>
              <a href="#" class="square_btn" onclick="aaa()">NaoyaOshiro</a>
              <canvas id="myChart"></canvas>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
            </div>

            <!-- <div>
                <h2>LED</h2>
                LED0: <input type="checkbox" id="checkbox-led-0" name="checkbox-led-0" data-on-color="primary" onclick="setLed('0', this.checked)"><br>
                LED1: <input type="checkbox" id="checkbox-led-1" name="checkbox-led-1" data-on-color="primary" onclick="setLed('1', this.checked)"><br>
                LED2: <input type="checkbox" id="checkbox-led-1" name="checkbox-led-1" data-on-color="primary" onclick="setLed('2', this.checked)"><br>
                <hr>
            </div>
            <div>
                <h2>Button</h2>
                Button0: <input type="checkbox" id="checkbox-button-0" name="checkbox-button-0" data-on-color="primary"><br>
                Button1: <input type="checkbox" id="checkbox-button-1" name="checkbox-button-1" data-on-color="primary">
                <hr>
            </div> -->
        </div>
        </main>
        <!-- load script files -->
        <!-- <script type="text/javascript" src="static/js/caller.js" charset="utf-8"></script> -->
        <script type="text/javascript" src="static/js/caller.js" charset="utf-8"></script>
    </center>
    </body>
</html>
