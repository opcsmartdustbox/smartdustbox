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


        <!-- <p class="shadow"><div class="foo">
          <span class="letter" data-letter="S">S</span>
          <span class="letter" data-letter="m">m</span>
          <span class="letter" data-letter="a">a</span>
          <span class="letter" data-letter="r">r</span>
          <span class="letter" data-letter="t">t</span>
          <span class="letter" data-letter="D">D</span>
          <span class="letter" data-letter="u">u</span>
          <span class="letter" data-letter="s">s</span>
          <span class="letter" data-letter="t">t</span>
          <span class="letter" data-letter="B">B</span>
          <span class="letter" data-letter="o">o</span>
          <span class="letter" data-letter="x">x</span>
        </div></p> -->
            <div>
                <br>
                <h2>test_checkbox</h2>

                    <label>
                      <input type="checkbox" name="checkbox01[]" class="checkbox01-input" onclick="setLed('0', this.checked)">
                      <span class="checkbox01-parts">LED00</span><br><br>
                    </label>
                <hr>
            </div>



            <div id="txt">ここにデータを表示</div>             <!-- データを表示するdiv要素 -->
            <script>
            var alpha = 0, beta = 0, gamma = 0;             // ジャイロの値を入れる変数を3個用意

            // ジャイロセンサの値が変化したら実行される deviceorientation イベント
            window.addEventListener("deviceorientation", (dat) => {
                alpha = dat.alpha;  // z軸（表裏）まわりの回転の角度（反時計回りがプラス）
                beta  = dat.beta;   // x軸（左右）まわりの回転の角度（引き起こすとプラス）
                gamma = dat.gamma;  // y軸（上下）まわりの回転の角度（右に傾けるとプラス）
            });

            // 指定時間ごとに繰り返し実行される setInterval(実行する内容, 間隔[ms]) タイマーを設定
            var timer = window.setInterval(() => {
                displayData();      // displayData 関数を実行
            }, 33); // 33msごとに（1秒間に約30回）

            // データを表示する displayData 関数
            function displayData() {
                var txt = document.getElementById("txt");   // データを表示するdiv要素の取得
                txt.innerHTML = "alpha: " + alpha + "<br>"  // x軸の値
                              + "beta:  " + beta  + "<br>"  // y軸の値
                              + "gamma: " + gamma;          // z軸の値
            }

            callApi(
                SERVER_URL + "setLed",
                {
                    "num": num,
                    "onoff": onoff
                },
                function (o) {
                });

            function callApi(url, jsonObj, callback) {
                var xhr = new XMLHttpRequest();
                xhr.open('POST', url);
                xhr.setRequestHeader('Content-Type', 'application/json');
                xhr.setRequestHeader('Accept', 'application/json');

                xhr.onreadystatechange = (function(myxhr) {
                    return function() {
                        if (xhr.readyState == 4 && xhr.status == 200) {
                            callback(myxhr);
                        }
                    }
                })(xhr);

                xhr.send(JSON.stringify(jsonObj));
            }
            </script>


            <div>
                <h2>LED</h2>
                LED0: <input type="checkbox" id="checkbox-led-0" name="checkbox-led-0" data-on-color="primary" onclick="setLed('010', this.checked)"><br>
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
