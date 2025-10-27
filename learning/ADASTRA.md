# Ad Astra Addon Tutorial
Wanna make an addon for Ad Astra ? You are in the good place !

Adding a planet in ad Astra is very easy.
But for now, you need to follow 

## Ad Astra Addon 101

### 1) Create our dimension 
To create our dimension we need to create two folders in *data/modid/* :

- dimension : in this folder, you will need to create a file for all your dimensions where you'll put your dimension info like :
    - the type : here *modid:your_planet*
    - the generator : the minecraft worldgen or a custom one 
    - the biomes sources : which biomes do you want to have in your dimension 

- dimension_type : in this folder, you will need to create a file for all your dimensions where you'll put information like :
    - ambient_light
    - bed_works
    - effects : be sure to use modid:your_planet

‼️ attention : you will need to make a dimension for your planet AND your planet's orbit. For you planet idea, you need to use *ad_astra:orbit* for the settings and *ad_astra:orbit* for the biome.

### 2) Create the Planet Data
In *data/modid/planet_data/planets/* you will need to create a file name like your planet and add theses information :
```json
{
  "translation": "gui.modid.text.yourplanet",
  "galaxy": "modid:your_galaxy", //We create on later in this "tutorial"
  "solar_system": "modid:your_solar_system", // Same here
  "world": "modid:your_planet",
  "orbit_world": "modid:your_planet_orbit",
  "rocket_tier": 4,
  "gravity": 3.721,
  "has_atmosphere": true,
  "days_in_year": 365,
  "temperature": -20,
  "solar_power": 17,
  "orbit_solar_power": 19,
  "has_oxygen": true,
  "button_color": "light_blue"
}
``` 

### 3) The Resource pack Part 
To have a cool and working (it's important) addon, you need to add theses four folders in *assets/modid/planet_resources* :

- galaxy : In Ad Astra, there is one galaxy : the milky_way. If you want to add an other galaxy, create a files with the name of your galaxy and put this into the file :
```json
{
  "galaxy": "modid:your_galaxy",
  "texture": "modid:textures/sky/your_galaxy.png",
  "button_color": "purple",
  "scale": 250
}
```

- solar_systems : in Ad Astra, there is two solar system : the solar_system and proxima _centory. To add an other solar system, create a file with the name of your new solar system and add this :
```json 
{
  "galaxy": "modid:your_galaxy", //The galaxy of the solar sytem
  "solar_system": "modid:your_solar_system", 
  "sun": "ad_astra:textures/sky/gui/blue_sun.png", 
  "sun_scale": 18,
  "button_color": "turquoise",
  "ring_color": {
    "r": 0,
    "g": 128,
    "b": 128,
    "a": 200
  }
}
```

- planet_rings : in the planet_rings folder, there are two folders : one for each solar_system So you'll need to create an other one and create a file with the name of your planet and add this :
```json
{
  "galaxy": "modid:your_galaxy",
  "solar_system": "modid:your_solar_system",
  "texture": "modid:textures/sky/your_planet.png",
  "speed": 88,
  "scale": 8, //The size of your planets
  "radius": 1.0 //Here, it's the firts planet in the solar system
}
```
‼️ : this file was only for the Planet Selection Screen

- sky_renderers : this folder is important for the player immersion. In the folder, you will need to create a file for each dimension and orbit you will add UNLESS if you don"t want to change something in the sky.
Here an exemple for an orbit : 
```json
{
    "world": "modid:your_planet_orbit",
    "stars": {
        "fancy_count": 13000,
        "fast_count": 6000,
        "colored_stars": true,
        "daylight_visible": true
    },
    "sunset_color": "vanilla",
    "dimension_effects": {
        "type": "none"
    },
    "cloud_effects": "none",
    "weather_effects": "none",
    "horizon_angle": 0,
    "sky_objects": [
        {
            "texture": "ad_astra:textures/sky/sun.png", // The texture of the sky of your solar_system
            "blending": true,
            "render_type": "dynamic",
            "scale": 50.0,
            "rotation": [
                0.0,
                -90.0,
                0.0
            ]
        },
        {
            "texture": "modid:textures/sky/your_planet.png",
            "blending": false,
            "render_type": "scaling",
            "scale": 1.0,
            "rotation": [
                180.0,
                180.0,
                0.0
            ]
        },
        {
            "texture": "ad_astra:textures/sky/light.png", //The effect of the light for the planet
            "blending": true,
            "render_type": "scaling",
            "scale": 3.0,
            "color": {
                "r": 255,
                "g": 204,
                "b": 153
            },
            "rotation": [
                180.0,
                180.0,
                0.0
            ]
        }
    ]
}
```

### 4) The translation part (Aka : the last one)
Now you have successfully (i hope) create a new planet/solar system/galaxy !
But they should have name (It's better)
In your folder *assets/modid/lang* add a file name en_us.json and add this (if you know modding, this part is a piece of cake) :
```json
{
  "gui.modid.text.yourplanet": "My Planets",
  "gui.modid.text.your_galaxy": "My Galaxy",
  "gui.swplanets.text.your_solar_system": "My Solar System"

}
```

Now, you should have a new planet in the Planet Selection Screen !

If you need more informations about worldgen, you should look at this site : https://misode.github.io/worldgen/

### **You should see the Ad Astra wiki too ! [https://github.com/terrarium-earth/Ad-Astra/wiki](https://github.com/terrarium-earth/Ad-Astra/wiki)**
