
local response = game:GetService("HttpSerive"):GetAsync("http://httpbin.org/get")
print(game:GetService("HttpSerive"):JSONDecode(response).origin)
