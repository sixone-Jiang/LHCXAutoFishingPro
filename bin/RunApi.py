from common import PathUtils, ConfigUtils
from common.Location import Location
from bin.StartFish import StartFish
import time


class RunApi:
    # 钓鱼
    def run_fish(adb, d, baits_list=[]):
        work_dir = PathUtils.get_work_dir()
        times = int(ConfigUtils.get('end_times'))
        new_fish_stop = int(ConfigUtils.get('new_fish_stop'))
        # 自行测量屏幕中钓鱼显示框左边界和上边界位置950-605
        mumu_left = int(ConfigUtils.get('mumu_left'))
        mumu_top = int(ConfigUtils.get('mumu_top'))
        # 自行找一个屏幕中方便点击的初始点（要位于模拟器内）
        click_x_origin = int(ConfigUtils.get('x_origin'))
        click_y_origin = int(ConfigUtils.get('y_origin'))

        for i in range(times):
            print('第{%d}轮钓鱼开始'%i)
            adb.click(work_dir + '/temp_images/fish.png')
            time.sleep(3)
            StartFish.choice_rod_bait(baits_list,work_dir + '/temp_images/baits/', adb=adb)
            adb.click(work_dir +'/temp_images/start2.png')
            # 等待钓鱼开始 5-10s
            time.sleep(5)
            now = time.time()
            ring_flag = now 
            flag = 0

            while time.time() - now <60*5:
                StartFish.window_capture(d=d,filename=work_dir+'/temp_images/screen_fish.jpg',mumu_left=mumu_left,mumu_top=mumu_top)
                x, y = StartFish.get_position(image_path=work_dir+'/temp_images/screen_fish.jpg')
                ring_flag ,flag = StartFish.Stage(d, x, y, ring_flag, flag, click_x_origin, click_y_origin)
                # 判断是否为新鱼
                if new_fish_stop > 0:
                    # 该参数如果异常请自行测定
                    StartFish.window_capture(d=d, filename=work_dir+'/temp_images/screen_fish_2.jpg',mumu_left=mumu_left+500-320,mumu_top=mumu_top+593-204-30, mumu_width=160+40+120, mumu_h=40+60)
                    if StartFish.is_new_fish(work_dir+'/temp_images/new_fish/', work_dir):
                        new_fish_stop -= 1
                        print("已经捕捉到新鱼")
                    else :
                        #print("捕捉到的不是新鱼")
                        pass
                    if new_fish_stop == 0:
                        return None
                # 若超时计时器超时，则立即进入下一轮钓鱼
                if time.time() - ring_flag >9:
                    break
            print('—————————本轮结束————————')
            
            ending_loc = Location(adb, None, 600, 600)
            ending_loc.click()
            ending_loc.click()
            ending_loc.click()
            
            
                
        
            
            

            

