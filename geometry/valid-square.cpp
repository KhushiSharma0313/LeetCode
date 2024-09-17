// takes 4 points of square, and six distances between them - 4 sides being equal and 2 sides (diagonal) are larger than sides
//based on pythagoras theorem, 
// a^2 + b^2 = c^2
// since sides of square are equal - a^2 + a^2 = d^2(d is diagonal here)
// d^2 = 2a^2 
// to check if it's square or not, check this relation 
// difference between these points 
// put difference of these points in unordered set - since it's used to store unique elements 
// it should only have 2 elements, since only 2 unique values
class Solution {
public:

int d(vector<int>& p1, vector<int>& p2) {
    return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]);
}

bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
    unordered_set<int> s({ d(p1, p2), d(p1, p3), d(p1, p4), d(p2, p3), d(p2, p4), d(p3, p4) });
    return !s.count(0) && s.size() == 2;
}
};