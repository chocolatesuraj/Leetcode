class MinStack {
public:
    std::vector<std::array<int,2>> stack;
    MinStack() {
        
    }
    
    void push(int val) {
        int min;
        if(this->stack.size()==0)
            {min=val;}
        else
            {min=this->stack.back()[1];}
        std::array newele={val,std::min(min,val)};
        this->stack.push_back(newele);
        
    }
    
    void pop() {
        this->stack.pop_back();
        
    }
    
    int top() {
        return this->stack.back()[0];
        
    }
    
    int getMin() {
        return this->stack.back()[1];
        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
