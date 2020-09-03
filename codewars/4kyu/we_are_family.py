'''
We need a system that can learn facts about family relationships, check their
consistency and answer queries about them.
The task

Create a class Family with the following methods. All arguments are strings:
names of persons. Upon the first use of a name, that name is added to the family.

    male(name) and female(name) returning boolean

    Define the gender (corresponding to the method name) of the given person.
    Return False when these assignments cannot be made because of conflicts
    with earlier registered information.

    is_male(name) and is_female(name) returning boolean

    Return True when the person has the said gender. When no gender was assigned,
    both methods should return False

    set_parent_of(child_name, parent_name) returning boolean

    Defines the child-parent relationship between two persons. Returns False
    when the relationship cannot be made because of conflicts with earlier
    registered information.

    get_parents_of(name) and get_children_of(name) returning list of string

    Return the names of the person's parents/children in alphabetical order

Deducing information

When things can be implied from given information, it should be done.

For instance, a parent's gender can be determined as soon as the other parent's
gender becomes known:

fam = Family()
fam.set_parent_of("Vera", "George")
fam.set_parent_of("Vera", "Vanessa")
fam.female("Vanessa")
fam.female("George");  # False, because:
fam.is_male("George"); # ...this is True.

Also set_parent_of can return False. For example, if the relationship would infer
that one becomes their own ancestor:

fam = Family()
fam.set_parent_of("Vera", "George")
fam.set_parent_of("George", "Vera") # False

Details, rules, assumptions

Although the task relates to genealogy, the rules of this kata are not claimed to
be realistic. Several simplifications and rules apply, which may not hold in real life:

    Strings are case sensitive, but there are no tests playing around with
    "Peter", "PETER" and "PeTeR".
    People are uniquely identified by their name. For instance, there are no
    two different people called "Jim" in the same family.
    Once a person has an assigned gender, it cannot be changed.
    No gender conclusions should be made from personal names: "Bob" could well
    be a woman and "Susan" a man.
    People cannot have more than one mother and one father.
    The terms "parents" and "children" refer to the relatives in the immediate
    previous/next generations only, not to more remote ancestors or descendants.
    Incest may occur, so, for example, one's parent may at the same time be
    their grandparent.
    One cannot be their own ancestor.
    Age is not accounted for. Even if some incestuous relationships would infer
    that one's parent is more than 5 generations older, it should be allowed.
    In case a name's first occurrence is in a call of one of the two gender
    querying methods, the return value will always be false, as that new person
    does not have a known gender.
    In case a name's first occurrence is in a call of one of the two relation
    querying methods, the return value will always be an empty array/list, as
    there are no relationships known yet in which that new person participates.
    For the reasons in the preceding two bullet points it should not matter
    whether you actually store that name in these cases in your data structure,
    or not. In the latter case you would only store it at the next occasion when
    that name is mentioned in a call of one of the three other methods, that
    actually add information. The described interface has no way to query the
    difference between these two possible implementations, so you can choose freely.

Example

It could be created step by step with the following code — the expected return
value for each method call is indicated in comments:

fam = Family()
fam.set_parent_of("Frank", "Morgan")       # True
fam.set_parent_of("Frank", "Dylan")        # True
fam.male("Dylan")                          # True
fam.male("Dylan")                          # True, no conflict
fam.set_parent_of("Joy", "Frank")          # True
fam.male("Frank")                          # True
fam.male("Morgan")                         # False
# (Morgan is a woman because she both is Frank's parent, but not his father) 
fam.set_parent_of("July", "Morgan")        # True
# (The preceding assertion was rejected, so there is no conflict)
fam.is_male("Joy") or fam.is_female("Joy") # False
# (We know Joy is Frank's child, but we can't derive Joy's gender)
fam.get_children_of("Morgan")              # ["Frank", "July"]
fam.set_parent_of("Jennifer", "Morgan")    # True
fam.get_children_of("Morgan")              # ["Frank", "Jennifer", "July"]
fam.get_children_of("Dylan")               # ["Frank"]
# (That is all we know for sure)
fam.get_parents_of("Frank")                # ["Dylan", "Morgan"]
fam.set_parent_of("Morgan", "Frank")       # False
# (It is impossible to be the parent of your parent)
'''
class Person:

    def __init__(self):
        self.sex = None
        self.children = []
        self.parents = []

class Family:

    def __init__(self):
        self.members = dict()

    def get_parents_gap(self, first, second):
        if first not in self.members or second not in self.members:
            return None
        
        kids = self.members[first].children[:]
        parents, step = [first], 0
        while kids:
            parents_size = len(parents)
            for kid in kids:
                parents.extend([p for p in self.members[kid].parents if p not in parents])
                
            del parents[:parents_size]
            if second in parents:
                return step
            
            kids_size = len(kids)
            for parent in parents:
                kids.extend([k for k in self.members[parent].children if k not in kids])
                
            del kids[:kids_size]
            step += 1
            
        return None

    def get_parent_sex(self, name):
        kids = self.members.get(name, Person()).children[:]
        parents, kid_step = [name], 0
        while kids:
            parents_size = len(parents)
            for kid in kids:
                parents.extend([p for p in self.members[kid].parents if p not in parents])
                
            del parents[:parents_size]
            kids_size = len(kids)
            for parent in parents:
                person = self.members[parent]
                if person.sex == 'male':
                    return 'male' if kid_step%2 else 'female'
                elif person.sex == 'female':
                    return 'female' if kid_step%2 else 'male'
                kids.extend([k for k in person.children if k not in kids])
                
            del kids[:kids_size]
            kid_step += 1
            
        return None
        
    def male(self, name):
        person = self.members.get(name, Person())
        if person.sex == 'female':
            return False
        elif person.sex is None:
            if self.get_parent_sex(name) == 'female':
                return False
            
            person.sex = 'male'
            self.members[name] = person
            
        return True
    
    def is_male(self, name):
        if self.members.get(name, Person()).sex == 'male':
            return True
        
        return self.get_parent_sex(name) == 'male'
    
    def female(self, name):
        person = self.members.get(name, Person())
        if person.sex == 'male':
            return False
        elif person.sex is None:
            if self.get_parent_sex(name) == 'male':
                return False
            
            person.sex = 'female'
            self.members[name] = person
            
        return True

    def is_female(self, name):
        if self.members.get(name, Person()).sex == 'female':
            return True
        
        return self.get_parent_sex(name) == 'female'
    
    def set_parent_of(self, child_name, parent_name):
        if  child_name == parent_name:
            return False
        
        child = self.members.get(child_name, Person())
        parent = self.members.get(parent_name, Person())
        if child_name in parent.children:
            return True
        elif len(child.parents)==2:
            return False
        
        kids = child.children[:]
        while kids:
            if parent_name in kids:
                return False
            
            for _ in range(len(kids)):
                kids.extend(self.members[kids.pop(0)].children)
                
        fp_sex = None
        if child.parents:
            fp_sex = self.members[child.parents[0]].sex
            if fp_sex is None:
                fp_sex = self.get_parent_sex(child.parents[0])
                
        sp_sex = self.get_parent_sex(parent_name) if parent.sex is None else parent.sex
        if fp_sex==sp_sex and fp_sex is not None:
            return False
        
        if (fp_sex is None and sp_sex is None and
            child.parents and parent_name in self.members):
            gap = self.get_parents_gap(child.parents[0], parent_name)
            if gap is not None and gap%2:
                return False
            
        child.parents.append(parent_name)
        parent.children.append(child_name)
        self.members[child_name] = child
        self.members[parent_name] = parent
        return True
    
    def get_children_of(self, name):
        return sorted(self.members.get(name, Person()).children)
    
    def get_parents_of(self, name):
        return sorted(self.members.get(name, Person()).parents)
 
if __name__ == '__main__':
    fam = Family()
    print(fam.set_parent_of("Frank", "Morgan"))
    print(fam.set_parent_of("Frank", "Dylan"))
    print(fam.male("Dylan"))
    print(fam.male("Dylan"))
    print(fam.set_parent_of("Joy", "Frank"))
    print(fam.male("Frank"))                
    print(fam.male("Morgan"))
    print(fam.set_parent_of("July", "Morgan"))
    print(fam.is_male("Joy") or fam.is_female("Joy"))
    print(fam.get_children_of("Morgan"))
    print(fam.set_parent_of("Jennifer", "Morgan"))
    print(fam.get_children_of("Morgan"))            
    print(fam.get_children_of("Dylan"))             
    print(fam.get_parents_of("Frank"))              
    print(fam.set_parent_of("Morgan", "Frank"))    
