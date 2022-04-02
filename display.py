import cv2

def displayCar(model): # line 605

    if model == "WRX":
        car_filename = "subaru_wrx.jpeg"
    elif model == "STi":
        car_filename = "subaru_sti.jpeg"
    elif model == "BRZ":
        car_filename = "subaru_brz.jpeg"
    elif model == "Evolution X":
        car_filename = "mitsubishi_evolution_x.jpeg"
    elif model == "Eclipse GSX Turbo":
        car_filename = "mitsubishi_eclipse_gsx_turbo.jpeg"
    elif model == "Eclipse Spyder GTS":
        car_filename = "mitsubishi_eclipse_spyder_gts.jpeg"
    elif model == "Supra MK4":
        car_filename = "toyota_supra_mk4.jpeg"
    elif model == "Supra MK5":
        car_filename = "toyota_supra_mk5.jpeg"
    elif model == "Mustang GT":
        car_filename = "ford_mustang_gt.jpeg"
    elif model == "SVT Cobra":
        car_filename = "ford_svt_cobra.jpeg"
    elif model == "GT 500":
        car_filename = "ford_gt_500.jpeg.jpeg"
    elif model == "GT":
        car_filename = "ford_gt.jpeg"
    elif model == "Corvette":
        car_filename = "chevrolet_corvette.jpeg"
    elif model == "Camaro ZL1":
        car_filename = "chevrolet_camaro_zl1.jpeg"
    elif model == "Hellcat":
        car_filename = "dodge_hellcat.jpeg"
    elif model == "Redeye":
        car_filename = "dodge_redeye.jpeg"
    elif model == "Demon":
        car_filename = "dodge_demon.jpeg"
    elif model == "Viper":
        car_filename = "dodge_viper.jpeg"
    elif model == "Civic Type R":
        car_filename = "honda_civic_type_r.jpeg"
    elif model == "NSX":
        car_filename = "honda_nsx.jpeg"
    elif model == "GTR":
        car_filename = "nissan_gtr.jpeg"
    elif model == "Skyline R34":
        car_filename = "nissan_skyline_r34.jpeg"
    elif model == "370Z":
        car_filename = "nissan_370z.jpeg"
    elif model == "S15":
        car_filename = "nissan_s15.jpeg"
    elif model == "R8":
        car_filename = "audi_r8.jpeg"
    elif model == "TTS":
        car_filename = "audi_tts.jpeg"
    elif model == "RS":
        car_filename = "audi_rs.jpeg"
    elif model == "M3":
        car_filename = "bmw_m3.jpeg"
    elif model == "M5":
        car_filename = "bmw_m5.jpeg"
    elif model == "Roadster":
        car_filename = "tesla_roadster.jpeg"
    elif model == "Model 3":
        car_filename = "tesla_model_3.jpeg"
    elif model == "Aventador":
        car_filename = "lamborghini_aventador.jpeg"
    elif model == "Huracan":
        car_filename = "lamborghini_huracan.jpeg"
    elif model == "Veneno":
        car_filename = "lamborghini_veneno.jpeg"
    elif model == "448 GTB":
        car_filename = "ferrari_448_gtb.jpeg"
    elif model == "SF90":
        car_filename = "ferrari_sf90.jpeg"
    elif model == "LaFerrari":
        car_filename = "ferrari_laferrari.jpeg"
    elif model == "FXX-K":
        car_filename = "ferrari_ffx-k.jpeg"
    elif model == "720S":
        car_filename = "mclaren_720s.jpeg"
    elif model == "P1 Supercar":
        car_filename = "mclaren_p1_supercar.jpeg"
    elif model == "Senna":
        car_filename = "mclaren_senna.jpeg"

    # Open the image file
    imgOrig = cv2.imread('../Cars/' + car_filename)
    height, width = imgOrig.shape[:2]
    height = int(height)
    width = int(width)
    ratio = width / height
    while height > 600:
        height = height - 50
    while height < 550:
        height = height + 50
    width = round(height * ratio)
    img = cv2.resize(imgOrig, (width,height))



    # Displays the original image in the top left corner of the screen.
    image = 'Displaying Car Chosen'
    cv2.namedWindow(image)
    cv2.moveWindow(image, 0, 0)
    cv2.imshow(image, img)

    # Infinite loop to keep the windows open until the escape key is pressed.
    exit = False
    # Ask user if they want the car
    print('Do you want this car(y/n): ')
    while not exit:
        k = cv2.waitKey(1)
        if k == 121 or k == 110:
            cv2.destroyAllWindows()
            if k == 121:
                return 'yes'
            else:
                return 'no'

def displayMod(mod): # line 821
    if mod == "30mm Turbo":
        mod_filename = "30mm_turbo.jpg"
    elif mod == "50mm Turbo":
        mod_filename = "50mm_turbo.jpg"
    elif mod == "76mm Turbo":
        mod_filename = "76mm_turbo.jpg"
    elif mod == "Kraftwerks SuperCharger":
        mod_filename = "kraftwekrs_supercharger.jpg"
    elif mod == "Wieland SuperCharger":
        mod_filename = "wieland_supercharger.jpg"
    elif mod == "Hennessy SuperCharger":
        mod_filename = "hennessy_supercharger.jpg"
    elif mod == "GT Wing":
        mod_filename = "spoiler_gt_wing.jpeg"
    elif mod == "VRX Style Wing":
        mod_filename = "vrx_style_wing.jpg"
    elif mod == "Saleen Style Wing":
        mod_filename = "saleen_style_wing.jpg"
    elif mod == "Drag Wing":
        mod_filename = "drag_wing.jpg"
    elif mod == "Stage 1 Tune":
        mod_filename = "stage_1_tune.jpg"
    elif mod == "Stage 2 Tune":
        mod_filename = "stage_2_tune.jpg"
    elif mod == "Stage 3 Tune":
        mod_filename = "stage_3_tune.jpg"
    elif mod == "Stage 4 Tune":
        mod_filename = "stage_4_tune.jpg"
    elif mod == "Fuel Injectors":
        mod_filename = "fuel_injectors.jpg"
    elif mod == "Fuel Pump":
        mod_filename = "fuel_pump.jpg"
    elif mod == "E85 Fuel":
        mod_filename = "e85_fuel.jpg"
    elif mod == "Cold Air Intake":
        mod_filename = "cold_air_intake.jpg"
    elif mod == "Intake Filter":
        mod_filename = "intake_filter.jpg"
    elif mod == "Carbon Fiber BOdy Kit":
        mod_filename = "carbon_fiber_bodykit.jpg"
    elif mod == "Aero Style Body Kit":
        mod_filename = "aero_style_bodykit.jpg"
    elif mod == "Enkei RPF1 WHeels":
        mod_filename = "enkei_rpf1.jpg"
    elif mod == "Ohlins Road and Track Coilovers":
        mod_filename = "ohlins_road_and_track_coilovers.jpg"
    elif mod == "Autosport Control Arms":
        mod_filename = "autosport_control_arms.jpg"
    elif mod == "Sway Bar Kit":
        mod_filename = "sway_bar_kit.jpg"
    elif mod == "Bag Suspension System":
        mod_filename = "bag_suspension_system.jpg"
    elif mod == "Lowering Springs":
        mod_filename = "lowering_springs.jpg"
    elif mod == "Radiator Shrouds":
        mod_filename = "radiator_shrouds.jpg"
    elif mod == "Front Mount Intercooler Kit":
        mod_filename = "front_mount_intercooler.jpg"
    elif mod == "Coolant Overflow Tank":
        mod_filename = "coolant_overflow_tank.jpg"
    elif mod == "Silicone Radiator Hoses":
        mod_filename = "silicone_radiator_hoses.jpg"
    elif mod == "Stoptech Sport Brake Rotors":
        mod_filename = "stoptech_sport_brake_rotors.jpg"
    elif mod == "Hawk Performance Brake Pads":
        mod_filename = "hawk_performance_brake_pads.jpg"
    elif mod == "Stoptech Stainless Steel Brake Lines":
        mod_filename = "stoptech_stainless_steel_brake_lines.jpg"
    elif mod == "Cat-Back Exhaust System":
        mod_filename = "catback_exhaust.jpg"
    elif mod == "Straight Pipe Exhaust":
        mod_filename = "straight_pipe_exhaust.jpg"
    elif mod == "Exhaust Heat Shields":
        mod_filename = "exhaust_heat_shields.jpg"
    elif mod == "Drag Slicks":
        mod_filename = "drag_slicks.jpg"
    elif mod == "Performance Tires":
        mod_filename = "performance_tires.jpg"
    elif mod == "Touring Tires":
        mod_filename = "touring_tires.jpg"


    # Open the image file
    # Open the image file
    imgOrig = cv2.imread('../Mods/' + mod_filename)
    height, width = imgOrig.shape[:2]
    height = int(height)
    width = int(width)
    ratio = width / height
    while height > 600:
        height = height - 50
    while height < 550:
        height = height + 50
    width = round(height * ratio)
    img = cv2.resize(imgOrig, (width,height))
    # Displays the original image in the top left corner of the screen.
    image = 'Displaying Mod Chosen'
    cv2.namedWindow(image)
    cv2.moveWindow(image, 0, 0)
    cv2.imshow(image, img)

    # Infinite loop to keep the windows open until the escape key is pressed.
    exit = False
    # Ask user if they want the car
    print('Do you want this mod(y/n): ')
    while not exit:
        k = cv2.waitKey(1)
        if k == 121 or k == 110:
            cv2.destroyAllWindows()
            if k == 121:
                return 'yes'
            else:
                return 'no'