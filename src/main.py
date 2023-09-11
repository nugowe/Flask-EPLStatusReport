from flask import Flask, render_template_string

app=Flask(__name__)

@app.route("/getbash")
def home():
    import datetime
  
    target_date = datetime.datetime(2024, 5, 19)
    current_datetime = datetime.datetime.now()
    time_left = target_date - current_datetime
    days = {time_left.days}
    time = {time_left.seconds // 3600}
    minutes = {time_left.seconds // 60 % 60} 
    seconds = {time_left.seconds % 60}


    return(f"<h3><i><strong>THIS SEASON ENDS IN </strong> {time_left.days} days, {time_left.seconds // 3600} hours, {time_left.seconds // 60 % 60} minutes, {time_left.seconds % 60} seconds....</i></h3>")


@app.route("/daysleft")
def daysleft():
  from datetime import datetime
  EPLStartDate = datetime(2023, 8, 11, 21, 0)  
  EPLEndDate = datetime(2024, 5, 19, 0, 0)   
  EPLDuration = (EPLEndDate - EPLStartDate).days
  CurrentDate = datetime.now()
  EPLDurationTillDate = (EPLEndDate - CurrentDate).days
  EPLElapsedDays = EPLDuration - EPLDurationTillDate
  PercentagePlayingdaysleft=(EPLElapsedDays/EPLDuration)* 100
  PercentagePlayingdaysleft=round(PercentagePlayingdaysleft, 0)
  return(f"<h3><i>ABOUT </strong> {PercentagePlayingdaysleft}% </strong> OF GAMES PLAYED SO FAR....</i></h3>")


@app.route("/index")
def index():
    Chelsealogo = "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"
    Liverpoollogo = "https://upload.wikimedia.org/wikipedia/en/0/0c/Liverpool_FC.svg"
    ManchesterCitylogo = "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"
    ManchesterUnitedlogo = "https://upload.wikimedia.org/wikipedia/en/7/7a/Manchester_United_FC_crest.svg"
    Evertonlogo = "https://upload.wikimedia.org/wikipedia/en/7/7c/Everton_FC_logo.svg"
    Brightonlogo = "https://upload.wikimedia.org/wikipedia/en/f/fd/Brighton_%26_Hove_Albion_logo.svg"
    Brentfordlogo ="https://upload.wikimedia.org/wikipedia/en/2/2a/Brentford_FC_crest.svg"
    TottenhamHotspurlogo = "https://upload.wikimedia.org/wikipedia/en/b/b4/Tottenham_Hotspur.svg"
    WestHamlogo = "https://upload.wikimedia.org/wikipedia/en/c/c2/West_Ham_United_FC_logo.svg"
    AstonVillalogo = "https://upload.wikimedia.org/wikipedia/en/9/9f/Aston_Villa_logo.svg"
    Arsenallogo = "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"
    WolverhamptonWandererslogo = "https://upload.wikimedia.org/wikipedia/en/f/fc/Wolverhampton_Wanderers.svg"
    LutonTownlogo = "https://upload.wikimedia.org/wikipedia/en/9/9d/Luton_Town_logo.svg"
    CrystalPalacelogo = "https://upload.wikimedia.org/wikipedia/en/a/a2/Crystal_Palace_FC_logo_%282022%29.svg"
    Fulhamlogo = "https://upload.wikimedia.org/wikipedia/en/e/eb/Fulham_FC_%28shield%29.svg"
    Bournemouthlogo = "https://upload.wikimedia.org/wikipedia/en/e/e5/AFC_Bournemouth_%282013%29.svg"
    NewcastleUnitedlogo = "https://upload.wikimedia.org/wikipedia/en/5/56/Newcastle_United_Logo.svg"
    Nottinghamforestlogo = "https://upload.wikimedia.org/wikipedia/en/e/e5/Nottingham_Forest_F.C._logo.svg"
    Burnleylogo = "https://upload.wikimedia.org/wikipedia/en/6/6d/Burnley_FC_Logo.svg"
    SheffieldUnitedFClogo = "https://upload.wikimedia.org/wikipedia/en/9/9c/Sheffield_United_FC_logo.svg"
    template = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EPL | 2023/2024 Season</title>
     
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

   
   

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <!-- HTMX -->
    <script src="https://unpkg.com/htmx.org/dist/htmx.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Customize the width of carousel items */
        .strikers {
            flex-direction: column; /* Stack items vertically */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            height: 5vh; /* 100% of the viewport height */
            text-align: center;
        }
    </style>
    <style>
            .container {
            display: flex;
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            height: 10vh; /* Make the container at least as tall as the viewport */
        }

        /* Apply styles to the centered div */
            .topscorer {
                width: 100px; /* Set your desired width */
                padding: 20px; /* Add padding for content spacing */
                border: 1px solid #ccc; /* Border for visual separation */
        }
    </style>
    <style>
        /* Customize the width of carousel items */
        .carousel-inner .carousel-item {
            width: 20%; /* Adjust the width as needed */
            margin-left: auto;
            margin-right: auto;
        }
        .carousel-inner .carousel-item {
            height: 700px; /* Adjust the height as needed */
        }

        
    </style>
    <style>
    
        body {
            font-family: 'Lato', sans-serif;
            background-color: '#F0E68C';
            
        }
    </style>
    <style>
        .center-row {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 10vh;
        }

        .picture {
            width: 100px;
            height: 100px;
            margin: 0 10px;
        }
    </style>
    <style>
        .carousel slide {
            padding: 20px; 
        }
    </style>
    
</head>
<body>
    <nav class="navbar navbar-light"  style="background-color: #e3f2fd;">
        <a class="navbar-brand" href="https://www.premierleague.com/" >
          <img src="https://upload.wikimedia.org/wikipedia/en/f/f2/Premier_League_Logo.svg" width="150" height="40" class="d-inline-block align-top" alt="">
          
        </a>
        </strong></i></h4></center> List of Participating Teams 2023/2024 Season</strong></i></h4></center>
        
    </nav>
    <center><h4> <i><strong>PROMOTED TEAMS THIS SEASON</strong></i></h4></center>
    <div class="center-row">
    <img src={{ LutonTownlogo }} alt="Picture 1" class="picture">
    <img src={{ Burnleylogo }} alt="Picture 2" class="picture">
    <img src={{ SheffieldUnitedFClogo }} alt="Picture 3" class="picture">
</div>
<br></br>
</strong><center><div id="time" hx-get="/getbash" hx-trigger="every 1s"></center></strong>
</strong><center><div id="time_left" hx-get="/daysleft" hx-trigger="every 1s"></center></strong>
<div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src={{ Chelsealogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Liverpoollogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ ManchesterCitylogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ ManchesterUnitedlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Evertonlogo  }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Brightonlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Brentfordlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ TottenhamHotspurlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ WestHamlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ AstonVillalogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Arsenallogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ WolverhamptonWandererslogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ LutonTownlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ CrystalPalacelogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Fulhamlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Bournemouthlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ NewcastleUnitedlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Nottinghamforestlogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ Burnleylogo }} class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src={{ SheffieldUnitedFClogo }} class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
    

</html>
"""
    return render_template_string(template, Chelsealogo = Chelsealogo, Liverpoollogo = Liverpoollogo, ManchesterCitylogo = ManchesterCitylogo, ManchesterUnitedlogo = ManchesterUnitedlogo, Evertonlogo = Evertonlogo, Brightonlogo = Brightonlogo, Brentfordlogo = Brentfordlogo, TottenhamHotspurlogo = TottenhamHotspurlogo, WestHamlogo = WestHamlogo, AstonVillalogo = AstonVillalogo, Arsenallogo = Arsenallogo, WolverhamptonWandererslogo = WolverhamptonWandererslogo, LutonTownlogo = LutonTownlogo, CrystalPalacelogo = CrystalPalacelogo, Fulhamlogo = Fulhamlogo, Bournemouthlogo = Bournemouthlogo, NewcastleUnitedlogo = NewcastleUnitedlogo, Nottinghamforestlogo = Nottinghamforestlogo, Burnleylogo = Burnleylogo, SheffieldUnitedFClogo = SheffieldUnitedFClogo)

    