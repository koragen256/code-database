import xmltodict
import collections
import glob

def merge_dict(d, u):
    """ 
        Merge two dictionaries. Manage nested dictionary and multiple values with same key.
        Return merged dict 
    """
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            d[k] = merge_dict(d.get(k, {}), v)
        else:
            # No more nested
            if k in d:
                # Manage multiple values with same name
                if not isinstance(d[k], list):
                    # if not a list create one
                    d[k] = [d[k]]
                d[k].append(v)
            else:
                # Single value
                d[k] = v
    return d


if __name__ == "__main__":
    # Open input files

    globt = glob.glob("codes/*");

    #print(globt);
    temp ="";

    with open("file3.xml", "r",encoding="utf-8_sig") as file3_xml:

        temp = ""
        print(temp)
        for item in globt:
            with open(item, "r",encoding="utf-8_sig") as file1_xml:
                # Convert xml to dictionary
                # Merge dictionaries with special function
                temp = temp+file1_xml.read()
                print(item)

    with open("file3.xml", "w",encoding="utf-8_sig") as file3_xml:
        file3_xml.write(temp)