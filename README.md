<!DOCTYPE html>
<html style="font-family: sans-serif; touch-action: manipulation; zoom: 1.5;">
    <head>
        <title>Max Game</title>
    </head>
    <style>
        a {
			padding: 3px;
			font-size: large;
            text-decoration: none;
			cursor: pointer;
        }
        div#Clicky {
            display: flex;
            flex-direction: column;
        }
        .Space {
            height: 10px;
        }
        #Clicky {
            margin: 10px;
			padding: 5px;
			background-color: lightgray;
			border-radius: 10px;
        }
        #C {
            margin: 10px;
			padding: 5px;
            padding-block: 10px;
        }
    </style>
    <body>
        <h1>Max Game</h1>
        <div id="Clicky">
            <div style="display: flex;">
                <h3 style="margin-block: 7px;">Clicky</h3>
                <p style="margin: 12px; font-size: x-small;">(Mit Local Speicher)</p>
            </div>
            <a href="https://maxgamer999991.github.io/Max-Game/Clicky/Beta.html">Beta</a>
            <div class="Space"></div>
            <button onclick="Clicky.C = !Clicky.C; update()">Version</button>
            <div id="C">
                <div style="
                    padding: 3px;
			        font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
			        border: darkgray;
			        border-width: 3px;
			        border-style: solid;
			        border-radius: 10px;
                ">
                    <div style="
                        display: flex;
                        cursor: pointer;
                    " onclick="Clicky.v0 = !Clicky.v0; update()">
                        <p style="margin: 0; margin-left: 5px; margin-right: 10px;" id="C_V0_>">></p>
                        <p style="margin: 0;">V0.1 - V0.2</p>
                    </div>
                    <div id="C_V0" style="margin-block: 10px;">
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v0.1.html">V0.1</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v0.2.html">V0.2</a>
                    </div>
                </div>
                <div class="Space"></div>


                <div style="
                    padding: 3px;
			        font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
			        border: darkgray;
			        border-width: 3px;
			        border-style: solid;
			        border-radius: 10px;
                ">
                    <div style="
                        display: flex;
                        cursor: pointer;
                    " onclick="Clicky.v1 = !Clicky.v1; update()">
                        <p style="margin: 0; margin-left: 5px; margin-right: 10px;" id="C_V1_>">></p>
                        <p style="margin: 0;">V1.0 - V1.3</p>
                    </div>
                    <div id="C_V1" style="margin-block: 10px;">
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v1.0.html">V1.0</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v1.1.html">V1.1</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v1.2.html">V1.2</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v1.3.html">V1.3</a>
                    </div>
                </div>
                <div class="Space"></div>


                <div style="
                    padding: 3px;
                    font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
                    border: darkgray;
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 10px;
                ">
                    <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v2.0.html">V2.0</a>
                </div>
                <div class="Space"></div>


                <div style="
                    padding: 3px;
			        font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
			        border: darkgray;
			        border-width: 3px;
			        border-style: solid;
			        border-radius: 10px;
                ">
                    <div style="
                        display: flex;
                        cursor: pointer;
                    " onclick="Clicky.v3 = !Clicky.v3; update()">
                        <p style="margin: 0; margin-left: 5px; margin-right: 10px;" id="C_V3_>">></p>
                        <p style="margin: 0;">V3.0 - V3.1</p>
                    </div>
                    <div id="C_V3" style="margin-block: 10px;">
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v3.0.html">V3.0</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v3.1.html">V3.1</a>
                    </div>
                </div>
                <div class="Space"></div>


                <div style="
                    padding: 3px;
			        font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
			        border: darkgray;
			        border-width: 3px;
			        border-style: solid;
			        border-radius: 10px;
                ">
                    <div style="
                        display: flex;
                        cursor: pointer;
                    " onclick="Clicky.v4 = !Clicky.v4; update()">
                        <p style="margin: 0; margin-left: 5px; margin-right: 10px;" id="C_V4_>">></p>
                        <p style="margin: 0;">V4.0 - V4.1</p>
                    </div>
                    <div id="C_V4" style="margin-block: 10px;">
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v4.0.html">V4.0</a>
                        <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v4.1.html">V4.1</a>
                    </div>
                </div>
                <div class="Space"></div>


                <div style="
                    padding: 3px;
                    font-size: large;
                    text-decoration: none;
                    background-color: lightgray;
                    border: darkgray;
                    border-width: 3px;
                    border-style: solid;
                    border-radius: 10px;
                ">
                    <a href="file:///C:/Users/heide/Documents/GitHub/Max-Game/Clicky/Clicky%20v5.0.html">V5.0</a>
                </div>
            </div>
        </div>
    </body>
    <script>
        var Clicky = {
            C : false,
            v0 : false,
            v1 : false,
            v3 : false,
            v4 : false,
        }
        function update() {
            if (Clicky.C) {
                document.getElementById("C").style.display = "block";
                if (Clicky.v0) {
                    document.getElementById("C_V0_>").style.transform = "rotate(90deg)";
                    document.getElementById("C_V0").style.display = "block";
                } else {
                    document.getElementById("C_V0_>").style.transform = "rotate(0deg)";
                    document.getElementById("C_V0").style.display = "none";
                }
                if (Clicky.v1) {
                    document.getElementById("C_V1_>").style.transform = "rotate(90deg)";
                    document.getElementById("C_V1").style.display = "block";
                } else {
                    document.getElementById("C_V1_>").style.transform = "rotate(0deg)";
                    document.getElementById("C_V1").style.display = "none";
                }
                if (Clicky.v3) {
                    document.getElementById("C_V3_>").style.transform = "rotate(90deg)";
                    document.getElementById("C_V3").style.display = "block";
                } else {
                    document.getElementById("C_V3_>").style.transform = "rotate(0deg)";
                    document.getElementById("C_V3").style.display = "none";
                }
                if (Clicky.v4) {
                    document.getElementById("C_V4_>").style.transform = "rotate(90deg)";
                    document.getElementById("C_V4").style.display = "block";
                } else {
                    document.getElementById("C_V4_>").style.transform = "rotate(0deg)";
                    document.getElementById("C_V4").style.display = "none";
                }
            } else {
                document.getElementById("C").style.display = "none"
            }
        }

        window.addEventListener("resize", function() {
            document.body.style.zoom = Math.min(1, window.innerWidth / 400);
        });

        update()
    </script>
</html>
