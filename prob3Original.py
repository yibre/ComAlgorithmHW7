import argparse
import pickle as pk
import sys



def development(cities, roads, airports):
    roads_list = []
    airports_list = []
    return roads_list, airports_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cities", type=int, default=10, help="the number of cities")
    parser.add_argument("--roads", type=str, default="./roads.pk", help="road information")
    parser.add_argument("--airports",type =str, default = './airports.pk', help ="airports information")
    opt = parser.parse_args()

    cities = opt.cities

    f1 = open(opt.roads,"rb")
    f2 = open(opt.airports,"rb")

    roads = pk.load(f1)
    airports = pk.load(f2)

    f1.close()
    f2.close()

    road_list, airport_list = development(cities, roads, airports)

    print("Roads : ", end = "")
    print(road_list)

    print("Airports : ", end = "")
    print(airport_list)