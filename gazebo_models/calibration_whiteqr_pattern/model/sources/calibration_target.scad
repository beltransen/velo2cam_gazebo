difference(){
    translate([-2,-70,-50])
    cube([2,140,100]);

    union(){
        translate([-10,25,20])
            rotate([0,90,0])
            cylinder(h=20,r=12);
        translate([-10,25,-20])
            rotate([0,90,0])
            cylinder(h=20,r=12);   
        translate([-10,-25,20])
            rotate([0,90,0])
            cylinder(h=20,r=12);
        translate([-10,-25,-20])
            rotate([0,90,0])
            cylinder(h=20,r=12);
    }
}