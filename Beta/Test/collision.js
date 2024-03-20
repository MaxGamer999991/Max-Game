class _2D {
    Hit(x1, y1, x2, y2, x3, y3) {
        // if x3 and y3 in x1,y1 and x2,y2
        let x  =  x1 > x2  ?  x1 > x3 < x2  :  x2 > x3 < x1
        let y  =  y1 > y2  ?  y1 > y3 < y2  :  y2 > y3 < y1
        return x && y
    }
    Hit(x1, y1, x2, y2, x3, y3, x4, y4) {
        // if x3,y3 and x4,y4  in  x1,y1 and x2,y2
        let x  =  x1 > x2  ?  x1 > x3 < x2  :  x2 > x3 < x1
        let y  =  y1 > y2  ?  y1 > y3 < y2  :  y2 > y3 < y1
        return x && y
    }
}