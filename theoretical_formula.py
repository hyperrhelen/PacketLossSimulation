# CHAC, HELEN && TRUONG, NATHAN
# ECS 152A: FALL QUARTER
# DIPAK GHOSAL
# PROJECT PART 1

MU = 1

def packet_probability(arrival_rate, service_rate, buffer):
    sum = 0
    ro = arrival_rate/service_rate
    for i in range(0, buffer+2):
        #print(i)
        sum += ro**i
    p0 = 1 / sum
    return p0*(ro**(buffer+1))

def main():
    lambda_list = [0.2, 0.4, 0.6, 0.8, 0.9, 0.99]
    buffer_list = [10, 50]
    for buffer in buffer_list:
        print("Buffer: ", buffer)
        print("{0:<9} {1:<9}".format("Lambda", "Probability"))
        for arrival_rate in lambda_list:
            print("{0:<9} {1:<9.9f}".format(
                arrival_rate, round(packet_probability(arrival_rate, MU, buffer), 9)))
main()
