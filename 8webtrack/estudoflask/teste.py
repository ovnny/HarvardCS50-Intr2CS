symbol = request.form.get("symbol")
    quantity = request.form.get("quantity")
    today = datetime.today()
    day = today.strftime("%B, %d, %Y")
    hour = today.strftime("%H:%M:%S")
    
    if request.method == "POST":
        if not symbol:
            return apology("Missing the share symbol", 403)

        elif not int(quantity) or int(quantity) < 0:
            return apology("Must provide share's quantity. Only integers allowed.", 403)

        
        quote = lookup(symbol)
        quoted = list(quote.values())
        format(quoted[1], '.2f')
        quoted.extend((quantity, day, hour))
            
        foreign_key = db.execute("SELECT user_id FROM users WHERE user_id = user_id")
        user_id = foreign_key
        buying_process(user_id[0]['user_id'], quoted[1], quoted[3])
        
        db.execute("""
                    INSERT INTO userbuy(
                    symbol, name, quantity, price, day, hour, user_id)
                    VALUES (?, ?, ?, ?, ?, ?, ?)""",
                    quoted[2], quoted[0], quoted[3], quoted[1],
                    quoted[4], quoted[5], user_id[0]['user_id'])
                        
                    #[name price symbol quantity day hour]
            
        return render_template("/bought.html", quoted=quoted)

    return render_template("/buy.html")

  
    def buy_process(int(quantity), currentPrice, fonds):
    totalBuy = int(quantity) * float(currentPrice)
    format(totalPurchase, '.2f')

    if not fonds:
        return apology("You have no fonds to aquire the assets", 403)
    elif fonds < totalbuy:
        return apology("You have no fonds to aquire the assets", 403)

    Cash = fonds - totalBuy
    updatedStatus = [Cash, totalBuy]
        
    return updatedStatus

def setNewStatus():
  db.execute(
            "UPDATE users SET cash = ? WHERE user_id = user_id", updatedStatus[0];
            "UPDATE userbuy SET TOTAL = ? WHERE user_id = user_id", updatedStatus[1]
  )
