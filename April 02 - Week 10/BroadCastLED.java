// A java class to get the status of LED from Firebase database
// Whenever the status of light changes i.e. ON to OFF or vice versa.
// A broadcast is received on the android app in the form of toast.

package com.example.text_to_speech;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.widget.Toast;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

/**
 * Created by piyus on 2018-04-06.
 */

public class BroadCastLED extends BroadcastReceiver {

    private DatabaseReference myRef1;
    @Override
    public void onReceive(final Context context, Intent intent) {

        myRef1 = FirebaseDatabase.getInstance().getReference().child("LED");

        myRef1.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(DataSnapshot dataSnapshot)
            {
                String value = dataSnapshot.getValue(String.class);
                Toast.makeText(context, "LED is "+value, Toast.LENGTH_LONG).show(); // A toast to inform the user that LED status has changed
            }

            @Override
            public void onCancelled(DatabaseError databaseError) {

            }
        });
    }
}
