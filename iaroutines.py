from oshelper import *
from uihelper import *
from routines import *

def color_map_move(x, y, current_time, color_map='color_map.png', mapped_regions=[]):
    x_init_minimap = 1645;
    y_init_minimap = 805;

    # ex: x = 1780 and y = 940; x > 1645 -> x = x - 1645 -> x = 135;  y > 805 -> y = y - 805 -> y = 135; 
    
    if x > 1645:
        x -= 1645;
    if y > 805:
        y -= 805;

    print('x: '+ str(x) + ', y: '+str(y));
    if len(mapped_regions)==0:
        mapped_regions = [
                      {
                        "color": {"red": 255, "blue": 0, "green": 0}, 
                        "corlor_label": "red",
                        "label": "alcance_t1_mid_inimiga",
                        "avoid": .6,
                        "ignore_past_time": 10.0,
                      },
                      {
                        "color": {"red": 0, "blue": 255, "green": 0}, 
                        "corlor_label": "blue",
                        "label": "alcance_t2_mid_inimiga",
                        "avoid": .6,
                        "ignore_past_time": 14.0,
                      },
                      {
                        "color": {"red": 0, "blue": 0, "green": 255}, 
                        "corlor_label": "green",
                        "label": "alcance_t3_mid_inimiga",
                        "avoid": .6,
                        "ignore_past_time": 16.0,
                      },
                    ]

        # print(mapped_regions)
    color_map = Image.open(color_map);
    target_coordinate = x, y
    target = color_map.getpixel(target_coordinate);
    print('target: '+ str(target));
    result = 0.5;
    result_default = True;
    
    for mapped_region in mapped_regions:
        print('target: '+ str(target));
        print('mapped_region_color: ('+str(mapped_region['color']['red'])+ ', '+str(mapped_region['color']['green'])+', '+str(mapped_region['color']['blue']) + ')');        
        if target[0] == mapped_region['color']['red']:
            if target[1] == mapped_region['color']['green']:
                if target[2] == mapped_region['color']['blue']:
                    if current_time <= mapped_region['ignore_past_time']:
                        print('x and y matched: ' + mapped_region['label'])
                        result_default = False;
                        if mapped_region['avoid'] >= .5: # if avoid > .5
                            result = 0.1; # result = 0.1 (0.1 almost impossible, 0.0 impossible, 0.2-0.4 likely but no, 0.5-0.9 yes, 1.0 sure)
                    else:
                        print('failed due to ignore_past_time');

    return result;
                
