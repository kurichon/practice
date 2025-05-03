#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

struct Node {
    int key, value;
    Node* prev;
    Node* next;
    Node(int k, int v) : key(k), value(v), prev(nullptr), next(nullptr) {}
};

class Cache
{
protected:
unordered_map<int, Node*> mp; //map int,Node* (key,value)
int cp; //capacity
Node *head, *tail;

public:
Cache(int capacity) : cp(capacity) {}
virtual void set(int key, int value) = 0;
virtual int get(int key) = 0;
};

class LRUCache: public Cache{
public:
    LRUCache(int capacity) : Cache(capacity) {}
    void moveToHead(Node* node){
        if (node == head)
        {//already at the head
            return;
        } 
        
        // Unlink
        if (node->prev) 
        {//if a previous node exists
            
        node->prev->next = node->next; 
        }
        if (node->next)
        {//if a next node exists
        node->next->prev = node->prev;
        }
        if (node == tail)
        {//if node is at tail, the previous node is the new tail
            tail = node->prev;
        }
        node->prev = nullptr;
        node->next = head;
        
        if (head)
        {//if there is a head previously
            head->prev = node;
        }
        head = node; //node is new head
        if (!tail)
        {
            tail = head;
        } //only 1 node left, so head == tail
    }
    void removeTail()
    {
        if (!tail) 
        {
            return; //list is empty
        }
        mp.erase(tail->key); //remove key from map
        Node* prev = tail->prev; //reallocate pointer
        delete tail;
        
        if (prev)
        {
            prev->next = nullptr; //update linkedlist (prev is the new tail)
        }
        else 
        {
            head = nullptr; //only one node existed so list is now empty
        }
        tail = prev; //update new tail
    }
    void addToHead(Node* newNode){
        if(newNode == head)
        {
            return;
        }
        newNode->next = head;
        newNode->prev = nullptr; //new head
        
        
        if(head) //if list has head
        {//update old head node to point to new node
            head->prev = newNode;
        }
        
        head = newNode;
        if (!tail){ //if list was empty newNode is also tail
          tail = newNode;   
        } 
    }
    
    int get(int key) override{
       if(mp.find(key) != mp.end())
       {
        Node* node = mp[key];
        return node->value;
       } //is in cache
       else {
       return -1;
       } 
    }
    void set(int key,int value) override{
        if(mp.find(key) != mp.end())
        {
            Node* node = mp[key];
            node->value = value;
            moveToHead(node);
            //is in cache move to head
        }
        else
        {
        if ((int)mp.size() == cp)
        {
            removeTail();
        }
        //not found in cache, create new head, if full remove tail
            Node* newNode = new Node(key, value);
            addToHead(newNode);
            mp[key] = newNode;
        } 
    }            
};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    //get input N number of lines, M capacity of cache
    int N,M;
    int key,value;
    string command;
    cin>>N>>M;
    Cache *cachepointer = new LRUCache(M);
    for(int i = 0;i<N;i++)
    {
        cin>>command;
        if(command == "set")
        {
            cin>>key>>value;
            cachepointer->set(key,value);
        }//do set
        else if (command == "get")
        {
            cin>>key;
            cout<<cachepointer->get(key)<<endl;
        } // do get
    }
    
    return 0;
}
