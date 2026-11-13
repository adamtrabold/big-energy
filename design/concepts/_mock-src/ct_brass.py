"""CATHEDRAL key material study in POV-Ray (director ruling 9: brass can't be judged as flat yellow).
OpenSCAD has no specular or reflection, so this renders the front-left corner of the base, keys and the PLAY-row
knobs with real metal shading. Geometry follows systems §10.2 (deck hole Ø 12, black carrier neck Ø 11.2 to deck
+ 2.8, a 12.7 head with a 1.2 rim and a low dome; head top deck + 6.8, H drawn 4.0). Plate R 7.7, block R 12.

    python3 ct_brass.py            # renders out/ct_brass_{A,B,C,macro}.png
"""
import math, os, subprocess, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
SHARPS = [8 + 18 * (i + 1) for i in (0, 1, 3, 4, 5, 7, 8, 10, 11, 12)]
NATS = [17 + 18 * n for n in range(15)]
KNOBS = [47, 67, 87, 143, 167]       # PLAY row y 68 (MOD, TUNE, GLIDE, EMPHASIS, AMOUNT); CUTOFF red at 119

HEAD = """
#declare Head = union {
  cylinder { <0,0,2.8>, <0,0,3.4>, 5.9 }
  torus { 5.95, 0.45 rotate x*90 translate z*3.25 }
  cylinder { <0,0,3.25>, <0,0,4.0>, 6.35 }
  intersection { sphere { 0, 6.35 scale <1,1,0.44> } plane { -z, 0 } translate z*4.0 }
}
"""

MATS = """
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
#declare BlackMatte = material { texture { pigment { rgb 0.028 } finish { ambient 0 diffuse 0.6 specular 0.12 roughness 0.06 } } }
#declare Cream = texture { pigment { rgb <0.93, 0.90, 0.83> } finish { ambient 0 diffuse 0.78 specular 0.05 roughness 0.1 } }
#declare Walnut = texture {
  pigment { bozo turbulence 0.3 color_map { [0 rgb <0.31,0.19,0.11>] [1 rgb <0.35,0.22,0.12>] } scale 20 }
  finish { ambient 0 diffuse 0.7 specular 0.08 roughness 0.08 } }
#declare Red = texture { pigment { rgb <0.62, 0.14, 0.09> } finish { ambient 0 diffuse 0.7 specular 0.15 roughness 0.05 } }
"""

STAGE = """
#version 3.7;
global_settings { assumed_gamma 1.0 max_trace_level 8 }
background { rgb <0.95, 0.93, 0.90> }
// studio: a big soft overhead box and a strip at the back so the domes have something to reflect
sky_sphere { pigment { gradient z color_map { [0 rgb <0.55,0.53,0.50>] [0.5 rgb <0.80,0.78,0.75>] [0.75 rgb <1.0,0.99,0.97>] [1 rgb <1.1,1.08,1.05>] } scale 2 translate -z } }
light_source { <-120, -260, 420> rgb 1.15 area_light <160,0,0>, <0,160,0>, 7, 7 adaptive 1 jitter circular orient }
light_source { <260, 300, 260> rgb 0.35 shadowless }
object { box { <-150,-400,-16.6>, <700, 700, -16.0> } texture { pigment { rgb <0.95,0.93,0.90> } finish { diffuse 0.85 ambient 0 } } }
object { box { <-2000, 900, -100>, <2000, 920, 900> } texture { pigment { rgb 1.6 } finish { ambient 1 diffuse 0 } } no_shadow }
"""

def rrect_prism(x0, y0, x1, y1, r, z0, z1):
    """a box with all four plan corners rounded r (POV union of boxes + cylinders)."""
    return (f"union {{ box {{ <{x0+r},{y0},{z0}>, <{x1-r},{y1},{z1}> }} box {{ <{x0},{y0+r},{z0}>, <{x1},{y1-r},{z1}> }} "
            + "".join(f"cylinder {{ <{cx},{cy},{z0}>, <{cx},{cy},{z1}>, {r} }} "
                      for cx, cy in ((x0 + r, y0 + r), (x1 - r, y0 + r), (x0 + r, y1 - r), (x1 - r, y1 - r))) + "}")

def knob(x, y):
    flutes = "".join(f"cylinder {{ <{x+7.55*math.cos(t)},{y+7.55*math.sin(t)},0.5>, <{x+7.1*math.cos(t)},{y+7.1*math.sin(t)},14>, 0.55 }} "
                     for t in (2 * math.pi * i / 24 for i in range(24)))
    return (f"difference {{ cone {{ <{x},{y},0>, 7.25, <{x},{y},12.5>, 6.8 }} union {{ {flutes} }} material {{ BlackMatte }} }}\n"
            f"cone {{ <{x},{y},12.5>, 6.75, <{x},{y},13.5>, 6.25 material {{ BlackMatte }} }}\n"
            f"box {{ <{x-0.35},{y+2.2},13.49>, <{x+0.35},{y+5.6},13.52> texture {{ pigment {{ rgb 0.95 }} finish {{ ambient 0.1 diffuse 0.8 }} }} }}\n")

def key(x, y, mat):
    return (f"cylinder {{ <{x},{y},-0.02>, <{x},{y},0.01>, 6.0 material {{ BlackMatte }} }}\n"
            f"cylinder {{ <{x},{y},-0.1>, <{x},{y},2.9>, 5.6 material {{ BlackMatte }} }}\n"
            f"object {{ Head material {{ {mat} }} translate <{x},{y},0> }}\n")

def board(nat, sh):
    s = f"object {{ difference {{ {rrect_prism(0, 0, 286, 108, 12, -15.6, 0)} {rrect_prism(4.3, 4.0, 281.7, 103.7, 7.7, -2.0, 1)} }} texture {{ Walnut }} }}\n"
    s += f"object {{ {rrect_prism(4.3, 4.0, 281.7, 103.7, 7.7, -2.0, 0)} texture {{ Cream }} }}\n"
    s += "".join(key(x, 13.5, nat) for x in NATS) + "".join(key(x, 36.0, sh) for x in SHARPS)
    s += "".join(knob(x, 68) for x in KNOBS)
    s += ("difference { cone { <119,68,0>, 10.4, <119,68,15>, 9.8 } union { "
          + "".join(f"cylinder {{ <{119+10.6*math.cos(t)},{68+10.6*math.sin(t)},0.5>, <{119+10.0*math.cos(t)},{68+10.0*math.sin(t)},16>, 0.6 }} "
                    for t in (2 * math.pi * i / 32 for i in range(32))) + "} texture { Red } }\n")
    return s

CAM_BOARD = "camera { location <-55, -150, 105> sky z look_at <62, 34, 4> angle 34 right -x*{ar} }\n"
CAM_MACRO = "camera { location <-6, -46, 30> sky z look_at <35, 22, 3> angle 30 right -x*{ar} }\n"

def render(name, scene, cam, w, h):
    os.makedirs(OUT, exist_ok=True)
    pov = os.path.join(OUT, name + ".pov")
    with open(pov, "w") as f:
        f.write(STAGE + MATS + HEAD + cam.replace("{ar}", f"{w / h:.4f}") + scene)
    png = os.path.join(OUT, name + ".png")
    subprocess.run(["povray", f"+I{pov}", f"+O{png}", f"+W{w}", f"+H{h}", "+A0.2", "+AM2", "+R3", "-D"],
                   check=True, capture_output=True)
    return png

def jobs(w=2000, h=1300):
    J = {
        "ct_brass_A": lambda: render("ct_brass_A", board("BrassPolished", "BlackMatte"), CAM_BOARD, w, h),
        "ct_brass_B": lambda: render("ct_brass_B", board("BlackMatte", "BrassPolished"), CAM_BOARD, w, h),
        "ct_brass_C": lambda: render("ct_brass_C", board("BrassPolished", "BrassPolished"), CAM_BOARD, w, h),
        # one polished and one aged (unlacquered, handled) sharp between black naturals: the lacquer question
        "ct_brass_macro": lambda: render("ct_brass_macro", board("BlackMatte", "BrassAged").replace(
            "object { Head material { BrassAged } translate <44,", "object { Head material { BrassPolished } translate <44,"), CAM_MACRO, w, h),
    }
    return J

if __name__ == "__main__":
    J = jobs(*( (800, 520) if "--test" in sys.argv else (2000, 1300) ))
    sel = [a for a in sys.argv[1:] if not a.startswith("--")] or list(J)
    for k in sel:
        print(J[k]())
