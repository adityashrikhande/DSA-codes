
def solve(image, x, y, old, new, m, n):
    if x < 0 or x == m or y < 0 or y == n or image[x][y] != old:
        return
        
    image[x][y] = new
    
    solve(image, x+1, y, old, new, m, n)
    solve(image, x-1, y, old, new, m, n)
    solve(image, x, y+1, old, new, m, n)
    solve(image, x, y-1, old, new, m, n)
    

def floodFill(image, x, y, newColor):
    # Write your Code here.
    if image[x][y] != newColor:
        solve(image, x, y, image[x][y], newColor, len(image), len(image[0]))
    
    return image