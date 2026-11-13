
#version 3.7;
global_settings { assumed_gamma 1.0 max_trace_level 8 }
background { rgb <0.95, 0.93, 0.90> }
// studio: a big soft overhead box and a strip at the back so the domes have something to reflect
sky_sphere { pigment { gradient z color_map { [0 rgb <0.55,0.53,0.50>] [0.5 rgb <0.80,0.78,0.75>] [0.75 rgb <1.0,0.99,0.97>] [1 rgb <1.1,1.08,1.05>] } scale 2 translate -z } }
light_source { <-120, -260, 420> rgb 1.15 area_light <160,0,0>, <0,160,0>, 7, 7 adaptive 1 jitter circular orient }
light_source { <260, 300, 260> rgb 0.35 shadowless }
object { box { <-150,-400,-16.6>, <700, 700, -16.0> } texture { pigment { rgb <0.95,0.93,0.90> } finish { diffuse 0.85 ambient 0 } } }
object { box { <-2000, 900, -100>, <2000, 920, 900> } texture { pigment { rgb 1.6 } finish { ambient 1 diffuse 0 } } no_shadow }

#declare BrassPolished = material { texture {
  pigment { rgb <0.80, 0.56, 0.26> }
  finish { ambient 0 diffuse 0.18 brilliance 3 specular 0.9 roughness 0.004 metallic
           reflection { 0.55, 0.85 metallic } } } }
// unlacquered, handled: the body tarnishes to dark gold-brown, the crown (touched) stays bright
#declare BrassAged = material { texture {
  gradient z
  texture_map {
    [0.00 pigment { rgb <0.27, 0.18, 0.09> } finish { ambient 0 diffuse 0.4 specular 0.2 roughness 0.04 metallic reflection { 0.06 metallic } } ]
    [0.89 pigment { rgb <0.30, 0.20, 0.10> } finish { ambient 0 diffuse 0.4 specular 0.2 roughness 0.04 metallic reflection { 0.06 metallic } } ]
    [0.96 pigment { rgb <0.80, 0.57, 0.27> } finish { ambient 0 diffuse 0.18 specular 0.9 roughness 0.006 metallic reflection { 0.5, 0.8 metallic } } ]
  }
  scale 6.8 } }
// black rhodium (1 um) over cast brass: the same weight and coldness as the brass keys, a dark glossy metal
#declare BlackPlated = material { texture {
  pigment { rgb <0.055, 0.055, 0.06> }
  finish { ambient 0 diffuse 0.25 brilliance 2 specular 0.6 roughness 0.008 metallic reflection { 0.18, 0.35 metallic } } } }
#declare BlackMatte = material { texture { pigment { rgb 0.028 } finish { ambient 0 diffuse 0.6 specular 0.12 roughness 0.06 } } }
#declare Cream = texture { pigment { rgb <0.93, 0.90, 0.83> } finish { ambient 0 diffuse 0.78 specular 0.05 roughness 0.1 } }
#declare Walnut = texture {
  pigment { bozo turbulence 0.3 color_map { [0 rgb <0.31,0.19,0.11>] [1 rgb <0.35,0.22,0.12>] } scale 20 }
  finish { ambient 0 diffuse 0.7 specular 0.08 roughness 0.08 } }
#declare Red = texture { pigment { rgb <0.62, 0.14, 0.09> } finish { ambient 0 diffuse 0.7 specular 0.15 roughness 0.05 } }

#declare Head = union {
  cylinder { <0,0,2.8>, <0,0,3.4>, 5.9 }
  torus { 5.95, 0.45 rotate x*90 translate z*3.25 }
  cylinder { <0,0,3.25>, <0,0,4.0>, 6.35 }
  intersection { sphere { 0, 6.35 scale <1,1,0.44> } plane { -z, 0 } translate z*4.0 }
}
camera { location <8, -30, 21> sky z look_at <40, 18, 3> angle 32 right -x*2.0000 }
object { difference { union { box { <12,0,-15.6>, <274,108,0> } box { <0,12,-15.6>, <286,96,0> } cylinder { <12,12,-15.6>, <12,12,0>, 12 } cylinder { <274,12,-15.6>, <274,12,0>, 12 } cylinder { <12,96,-15.6>, <12,96,0>, 12 } cylinder { <274,96,-15.6>, <274,96,0>, 12 } } union { box { <12.0,4.0,-2.0>, <274.0,103.7,1> } box { <4.3,11.7,-2.0>, <281.7,96.0,1> } cylinder { <12.0,11.7,-2.0>, <12.0,11.7,1>, 7.7 } cylinder { <274.0,11.7,-2.0>, <274.0,11.7,1>, 7.7 } cylinder { <12.0,96.0,-2.0>, <12.0,96.0,1>, 7.7 } cylinder { <274.0,96.0,-2.0>, <274.0,96.0,1>, 7.7 } } } texture { Walnut } }
object { union { box { <12.0,4.0,-2.0>, <274.0,103.7,0> } box { <4.3,11.7,-2.0>, <281.7,96.0,0> } cylinder { <12.0,11.7,-2.0>, <12.0,11.7,0>, 7.7 } cylinder { <274.0,11.7,-2.0>, <274.0,11.7,0>, 7.7 } cylinder { <12.0,96.0,-2.0>, <12.0,96.0,0>, 7.7 } cylinder { <274.0,96.0,-2.0>, <274.0,96.0,0>, 7.7 } } texture { Cream } }
cylinder { <17,13.5,-0.02>, <17,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <17,13.5,-0.1>, <17,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <17,13.5,0> }
cylinder { <35,13.5,-0.02>, <35,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <35,13.5,-0.1>, <35,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassAged } translate <35,13.5,0> }
cylinder { <53,13.5,-0.02>, <53,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <53,13.5,-0.1>, <53,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <53,13.5,0> }
cylinder { <71,13.5,-0.02>, <71,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <71,13.5,-0.1>, <71,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <71,13.5,0> }
cylinder { <89,13.5,-0.02>, <89,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <89,13.5,-0.1>, <89,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <89,13.5,0> }
cylinder { <107,13.5,-0.02>, <107,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <107,13.5,-0.1>, <107,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <107,13.5,0> }
cylinder { <125,13.5,-0.02>, <125,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <125,13.5,-0.1>, <125,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <125,13.5,0> }
cylinder { <143,13.5,-0.02>, <143,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <143,13.5,-0.1>, <143,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <143,13.5,0> }
cylinder { <161,13.5,-0.02>, <161,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <161,13.5,-0.1>, <161,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <161,13.5,0> }
cylinder { <179,13.5,-0.02>, <179,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <179,13.5,-0.1>, <179,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <179,13.5,0> }
cylinder { <197,13.5,-0.02>, <197,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <197,13.5,-0.1>, <197,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <197,13.5,0> }
cylinder { <215,13.5,-0.02>, <215,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <215,13.5,-0.1>, <215,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <215,13.5,0> }
cylinder { <233,13.5,-0.02>, <233,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <233,13.5,-0.1>, <233,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <233,13.5,0> }
cylinder { <251,13.5,-0.02>, <251,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <251,13.5,-0.1>, <251,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <251,13.5,0> }
cylinder { <269,13.5,-0.02>, <269,13.5,0.01>, 6.0 material { BlackMatte } }
cylinder { <269,13.5,-0.1>, <269,13.5,2.9>, 5.6 material { BlackMatte } }
object { Head material { BrassPolished } translate <269,13.5,0> }
cylinder { <26,36.0,-0.02>, <26,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <26,36.0,-0.1>, <26,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <26,36.0,0> }
cylinder { <44,36.0,-0.02>, <44,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <44,36.0,-0.1>, <44,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <44,36.0,0> }
cylinder { <80,36.0,-0.02>, <80,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <80,36.0,-0.1>, <80,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <80,36.0,0> }
cylinder { <98,36.0,-0.02>, <98,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <98,36.0,-0.1>, <98,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <98,36.0,0> }
cylinder { <116,36.0,-0.02>, <116,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <116,36.0,-0.1>, <116,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <116,36.0,0> }
cylinder { <152,36.0,-0.02>, <152,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <152,36.0,-0.1>, <152,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <152,36.0,0> }
cylinder { <170,36.0,-0.02>, <170,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <170,36.0,-0.1>, <170,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <170,36.0,0> }
cylinder { <206,36.0,-0.02>, <206,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <206,36.0,-0.1>, <206,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <206,36.0,0> }
cylinder { <224,36.0,-0.02>, <224,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <224,36.0,-0.1>, <224,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <224,36.0,0> }
cylinder { <242,36.0,-0.02>, <242,36.0,0.01>, 6.0 material { BlackMatte } }
cylinder { <242,36.0,-0.1>, <242,36.0,2.9>, 5.6 material { BlackMatte } }
object { Head material { BlackPlated } translate <242,36.0,0> }
