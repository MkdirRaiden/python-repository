class vector3D:
    x, y, z = 0, 0, 0
    def co_ordinates(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
def main():
    vec=vector3D()
    vec.co_ordinates(12, -3, -1)
    print(f"X: {vec.x}, Y: {vec.y}, Z: {vec.z}")
main()    