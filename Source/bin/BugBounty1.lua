
local response = game.HttpSerive:GetAsync("http://httpbin.org/get")
print(game.HttpService:JSONDecode(response).origin)
