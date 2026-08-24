def calculate_area(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height):
    flange1_area = flange1_width*flange1_height
    flange2_area = flange2_width*flange2_height
    web_area = web_width*web_height
    total_area = flange1_area+flange2_area+web_area
    return total_area

def calculate_centroid_beam(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height):
    centroid_flange1 = flange1_height/2
    centroid_flange2 = (flange1_height + web_height + (flange2_height/2))
    centroid_web = (flange1_height + (web_height/2))
    flange1_area = flange1_width*flange1_height
    flange2_area = flange2_width*flange2_height
    web_area = web_width*web_height
    total_area = flange1_area+flange2_area+web_area
    centroid_Y = (centroid_flange1*flange1_area + centroid_flange2*flange2_area + centroid_web*web_area)/total_area
    return centroid_Y

def calculate_moment_of_inertia(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height):
    centroid_flange1 = flange1_height/2
    centroid_flange2 = (flange1_height + web_height + (flange2_height/2))
    centroid_web = (flange1_height + (web_height/2))
    flange1_area = flange1_width*flange1_height
    flange2_area = flange2_width*flange2_height
    web_area = web_width*web_height
    total_area = flange1_area+flange2_area+web_area
    centroid_Y = (centroid_flange1*flange1_area + centroid_flange2*flange2_area + centroid_web*web_area)/total_area

    moi_flange1 = ((flange1_width*flange1_height**3)/12) + (flange1_area*(centroid_flange1-centroid_Y)**2)
    moi_flange2 = ((flange2_width*flange2_height**3)/12) + (flange2_area*(centroid_flange2-centroid_Y)**2)
    moi_web = ((web_width*web_height**3)/12) + (web_area*(centroid_web-centroid_Y)**2)
    net_moi = moi_flange1 + moi_flange2 + moi_web
    return net_moi

def calculate_bending_stress(moment, distance_from_centroid, net_moi):
    bending_stress = (moment*distance_from_centroid)/(2*net_moi)
    return bending_stress

def main():
    #Input geometrical parameters for I-beam 
    flange1_width = float(input("Enter the width of Flange1:"))
    flange1_height = float(input("Enter the height of Flange1:"))
    flange2_width = float(input("Enter the width of Flange2:"))
    flange2_height = float(input("Enter the height of Flange2:"))
    web_width = float(input("Enter the width of Web:"))
    web_height = float(input("Enter the height of Web:"))

    area = calculate_area(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height)
    
    distance_from_centroid = calculate_centroid_beam(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height)
    
    MOI = calculate_moment_of_inertia(flange1_width, flange1_height, flange2_width, flange2_height, web_width, web_height)
    
    #Input moment value for I-beam
    moment = float(input("Enter the value for moment:"))
    Bending_stress = calculate_bending_stress(moment, distance_from_centroid, MOI)
    print(f"\nTotal Area of I-Beam is: {area:.4f} mm^2")
    print(f"Total centroid of I-Beam is: {distance_from_centroid:.4f} mm")
    print(f"Total Moment of Inertia of I-Beam is: {MOI:.4f} mm^4")
    print(f"The Bending Stress of I-Beam is: {Bending_stress:.4f} MPa")

if __name__ == "__main__":
    main()
