func containsDuplicate(nums []int) bool {
    arr := make(map[int]bool)

    for _,num := range nums{
        if _, ok := arr[num]; ok {
            return true
        }else {
            arr[num] = true
        }
    }
    return false
}
