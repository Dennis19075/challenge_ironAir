
def segmentacionCli (customer_indices) : 
    segmentation = []
    for cli in range (len(customer_indices)):
        valueCli=customer_indices[cli]
        if valueCli%3==0 and valueCli %5==0:
            segmentation.append("Loyal-VIP")
        elif valueCli%3==0:
            segmentation.append("Loyal")
        elif valueCli%5==0:
            segmentation.append("VIP")
        else:
            segmentation.append("Regular")
    return segmentation