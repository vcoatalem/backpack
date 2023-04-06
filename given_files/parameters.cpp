#include <iostream>
#include <string>
#include <vector>
#include <memory>

class Parameters
{
    public:
    std::vector<int> itemWeights;
    std::vector<int> itemValues;
    int maxWeightCapacity;

    Parameters(const std::vector<int> weights, const std::vector<int> values, int maxWeightCapacity)
        : itemWeights(weights), itemValues(values), maxWeightCapacity(maxWeightCapacity)
    {
    }

    static std::unique_ptr<Parameters> easy()
    {
        auto values = std::make_unique<std::vector<int>>(std::initializer_list<int>{
            7250,
            421,
            7195,
            49,
            5077,
            1537,
            2229,
            5653,
            2366,
            6881
        });
        auto weights = std::make_unique<std::vector<int>>(std::initializer_list<int>{
            9818,
            4040,
            9560,
            9436,
            8080,
            793,
            886,
            4294,
            474,
            2929
        });
        return std::make_unique<Parameters>(*weights, *values, 5);
    }
};

int main(int argc, char** argv)
{
    std::unique_ptr<Parameters> params = Parameters::easy();
    for (int w : (params->itemWeights))
    {
        std::cout << w << " ";
    }
    std::cout << std::endl;
        for (int w : (params->itemValues))
    {
        std::cout << w << " ";
    }
    std::cout << std::endl;
    return 0;
}
