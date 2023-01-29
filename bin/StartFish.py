import time
import cv2
import os

def get_location_with_no_sc(temp_rel_path_list, work_dir, threshold=0.7):
        
        sp_gray = cv2.imread(work_dir+'/temp_images/screen_fish_2.jpg', cv2.COLOR_BGR2BGRA)

        if temp_rel_path_list:
            temp_abs_path = temp_rel_path_list
            temp_gray = cv2.imread(temp_abs_path, cv2.COLOR_BGR2BGRA)

            res = cv2.matchTemplate(sp_gray, temp_gray, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val < threshold:
                return False

            return True

        return False

class StartFish:
    base_rate = 1.0

    # 选择鱼饵
    def choice_rod_bait(baits_list , image_path, adb):
        if baits_list:
            for bait in baits_list:
                if adb.check(image_path+str(2*bait-1)+'.png'):
                    adb.click(image_path+str(2*bait-1)+'.png')
                    time.sleep(1)
                    break
                elif adb.check(image_path+str(2*bait)+'.png'):
                    adb.click(image_path+str(2*bait)+'.png')
                    time.sleep(1)
                    break
            return True
        else :
            return False

    # 判断新鱼
    def is_new_fish(image_path, work_dir):
        fish_list = os.listdir(image_path)
        #adb.screen_cap()
        if fish_list:
            for fish in fish_list:
                if get_location_with_no_sc(image_path+fish, work_dir):
                    return True
            return False
        else :
            return False
    
    # 屏幕抓取
    def window_capture(d, filename, mumu_left, mumu_top, mumu_width=650, mumu_h=3):
        img = d.screenshot() # x,y,w,h
        region = [mumu_left, mumu_top, mumu_left+mumu_width, mumu_top+mumu_h]
        img = img.crop(region)
        img.save(filename)

    # 区域长160 鱼长30
    # 区域：140 - 150 连续 8 个中投6个
    # 鱼：> 210 连续 8个中5个
    def get_position(image_path, region=160, fish=30):
        sp_gray = cv2.imread(image_path, cv2.COLOR_BGR2BGRA)
        # Alice 测量其像素长宽，取第一行,该段为理想段，也可根据个人需求增减18：642
        conp = sp_gray[1][18:638+4]
        red_green_index = -1
        white_index = -1
        for index in range(0, len(conp), 8):
            red_green = 0
            white = 0
            for k in range(8):
                comp = conp[index+k]
                if white_index == -1 and comp > 210:
                    white += 1
                if red_green_index == -1 and comp > 139 and comp <150:
                    red_green += 1
            if red_green >= 5:
                red_green_index = index
            if white > 4:
                white_index = index
        
        return red_green_index+region/2+10, white_index+fish/2
        
    def Stage(d, region, fish, ring_flag, flag, click_x_origin, click_y_origin):

        if region < fish:
            if flag == 0:
                d.touch.down(x=click_x_origin, y=click_y_origin)
                flag = 1
                #print('向右运动')
            return time.time(), flag
        else:
            d.touch.up(x=click_x_origin, y=click_y_origin)
            flag = 0
            #time.sleep(0.05)
            #print('向左运动')
            return ring_flag, flag